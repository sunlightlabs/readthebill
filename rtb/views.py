from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from feedinator.models import Feed, FeedEntry
from readthebill.rtb.forms import SignupForm
from readthebill.rtb.models import Organization
import gatekeeper
import urllib, urllib2

def index(request):
    
    is_thanks = ("thanks" in request.GET) and True or False
    
    if request.method == 'POST':
        
        form = SignupForm(request.POST)
        
        if form.is_valid():
            
            email = form.cleaned_data['email']
            zipcode = form.cleaned_data['zipcode']
            #affiliation = form.cleaned_data['affiliation']
            #message = form.cleaned_data.get('message', '')
            
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
                        
            bsd_url = "http://bsd.sunlightfoundation.com/page/s/rtbpetition"
            #params = {"email": email, "zip": zipcode, "custom-109": affiliation, "custom-108": message}
            params = {"email": email, "zip": zipcode, "firstname": first_name, "lastname": last_name}
            response = urllib2.urlopen(bsd_url, urllib.urlencode(params)).read()

            return HttpResponseRedirect('/?thanks')
            #return HttpResponseRedirect('http://bsd.sunlightfoundation.com/page/invite/readthebill')
    
    else:
        form = SignupForm()
        
    entries = gatekeeper.approved(FeedEntry.objects.all())
    return render_to_response("index.html", {"entries": entries, "form": form, "is_thanks": is_thanks }, context_instance=RequestContext(request))

def petition(request):
    return render_to_response("petition.html")

def photos(request):
    return render_to_response("photos.html", {"flickr_id": settings.FLICKR_ID, "flickr_tag": settings.FLICKR_TAG})

def support(request):
    return render_to_response("support.html", {"task_key": request.GET.get("task_key"), "username": request.GET.get("username"), "tcorps_url": settings.TCORPS_TASK_URL, "message": request.GET.get("message")})

def partners(request):
    partners = Organization.objects.order_by('name')
    return render_to_response("partners.html", {"partners": partners}, context_instance=RequestContext(request))

def partner_page(request, id):
    entry = FeedEntry.objects.get(pk=id)
    return render_to_response("partner_frame.html", {"entry": entry}, context_instance=RequestContext(request))

def press(request):
    feed = Feed.objects.get(codename="press")
    return render_to_response("press.html", {"feed": feed}, context_instance=RequestContext(request))

def rushed_bills(request):
    feed = Feed.objects.get(codename="rushedbills")
    return render_to_response("rushed_bills.html", {"feed": feed}, context_instance=RequestContext(request))
    
