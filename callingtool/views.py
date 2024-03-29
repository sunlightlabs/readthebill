import re
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.cache import cache
from django.utils.encoding import iri_to_uri
from django.contrib.auth.decorators import login_required

from simplesurvey.models import AnswerSet, Answer, Question, QuestionSet
from callingtool.models import LegislatorDetail

from sunlightapi import sunlight, SunlightApiError
sunlight.apikey = '0b738e1dc83d9ac6d619537c7d48e088'


STATES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)

STATE_DICT = dict(STATES)

def delete_url_cache(url):
    """ simple method to delete the cache for a particular URL """
    key_prefix = settings.CACHE_MIDDLEWARE_KEY_PREFIX
    cache_key = 'views.decorators.cache.cache_header.%s.%s' % (key_prefix,
                                                               iri_to_uri(url))
    cache.delete(cache_key)

def legislator_list(request):
    has_called = request.session.get('has_called', False)
    if has_called:
        del request.session['has_called']
    return render_to_response('callingtool/legislator_list.html',
                              {'legislator_list': LegislatorDetail.objects.exclude(legislator__title='Sen'),
                               'states': STATES,
                               'has_called': has_called})

def call_legislator(request, id):
    legislator = get_object_or_404(LegislatorDetail, id=id)
    calls = []
    for call in legislator.calls.all():
        cdict = {'date':call.date}
        for q,a in call.q_and_a():
            if a:
                cdict[q.text] = a.text
        calls.append(cdict)

    return render_to_response('callingtool/legislator_call.html',
                              {'legislator': legislator, 'calls': calls})

def state_reps(request, state):
    reps = LegislatorDetail.objects.filter(legislator__state=state).exclude(legislator__title='Sen')
    return render_to_response('callingtool/state_reps.html',
                              {'state_name': STATE_DICT[state],
                               'reps': reps})

def zip_rep(request, zipcode):
    oreps = sunlight.legislators.allForZip(zipcode)
    reps = []
    for o in oreps:
        if o.title!='Sen':
            qs = LegislatorDetail.objects.get(legislator__crp_id=o.crp_id)
            reps.append(  qs )
    return render_to_response('callingtool/zip_rep.html',
                              {'zipcode':zipcode, 'reps': reps})

def zip_direct(request, zipcode):
    from django.template.loader import get_template
    from django.template import Context
    from django.http import HttpResponse

    if zipcode=='00000':
        if request.POST['zip']:
            zipcode = request.POST['zip']
    oreps = sunlight.legislators.allForZip(zipcode)
    reps = []
    for o in oreps:
        if o.title!='Sen':
            qs = LegislatorDetail.objects.get(legislator__crp_id=o.crp_id)
            reps.append(  qs )
    t = get_template('callingtool/zip_rep.html')
    repblock = t.render(Context({'zipcode':zipcode, 'reps': reps}))

    return render_to_response('callingtool/legislator_list_nojs.html',
                              {'repblock':repblock})



def submit_call(request, id):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    # blank or zipcode
    zipcode = request.POST['zip']
    if not re.match('^(\d{5}(\-\d{4})?)?$', zipcode):
        return HttpResponseRedirect(reverse('legislator_list'))

    call = AnswerSet.objects.create(question_set=QuestionSet.objects.get(slug="readthebill-call"),
                                related_object=LegislatorDetail.objects.get(id=id))

    for q in request.POST.iterkeys():
        Answer.objects.create(answer_set=call,
                              question=Question.objects.get(text=q),
                              text=request.POST.get(q))

    request.session['has_called'] = id

    # clear related cache keys
    delete_url_cache('/')
    delete_url_cache('/state_reps/%s/' % LegislatorDetail.objects.get(pk=id).legislator.state)
    delete_url_cache('/call/%s/' % id)
    delete_url_cache('/all_calls/')

    return HttpResponseRedirect(reverse('legislator_list'))

def all_calls(request):
    calls = []
    for call in AnswerSet.objects.all().order_by('-date'):
        cdict = {'date':call.date, 'rep':call.related_object, 'id': call.id}
        for q,a in call.q_and_a():
            if a:
                cdict[q.text] = a.text
        calls.append(cdict)
    num_calls = len(calls)
    num_unique = Answer.objects.filter(question__text='email').values_list('text').distinct().count()
    num_sens = AnswerSet.objects.values_list('object_id').distinct().count()

    return render_to_response('callingtool/all_calls.html', {'calls': calls,
        'num_calls': num_calls, 'num_unique': num_unique, 'num_sens': num_sens})

@login_required
def delete_call(request, id):
    ans = AnswerSet.objects.filter(id=id)[0]
    pol_id = ans.object_id
    ans.delete()
    delete_url_cache('/call/%s/' % pol_id)
    delete_url_cache('/all_calls/')
    return HttpResponseRedirect(reverse('all_calls'))
