from django.conf.urls.defaults import *
from django.contrib import admin
from contact_form.forms import ContactForm

admin.autodiscover()

class RTBContactForm(ContactForm):
    from_email = "bounce@sunlightfoundation.com"
    recipient_list = ['jbrewer@sunlightfoundation.com']
    subject = "[ReadTheBill.org] Contact"

urlpatterns = patterns('',
    url(r'^admin/gatekeeper/', include('gatekeeper.urls')),
    url(r'^admin/(.*)', admin.site.root),
    url(r'^action/callspeakerboehner/', 'django.views.generic.simple.direct_to_template', {'template': 'action/boehner.html'}),
    url(r'^blog/', include('blogdor.urls')),
    url(r'^contact/', include('contact_form.urls'), {"form_class": RTBContactForm, "fail_silently": False}),
    url(r'^partners/', 'readthebill.rtb.views.partners', name="partners"),
    url(r'^partner/hat/', 'django.views.generic.simple.direct_to_template', {'template': 'partner_hat.html'}, name="partner_hat"),
    url(r'^partner/(?P<id>\d+)/', 'readthebill.rtb.views.partner_page', name="partner_page"),
    url(r'^petition/', 'readthebill.rtb.views.petition', name="petition"),
    url(r'^support/', 'readthebill.rtb.views.support', name="support"),
    url(r'^photos/', 'readthebill.rtb.views.photos', name="photos"),
    url(r'^press/', 'readthebill.rtb.views.press', name="press"),
    url(r'^rushed/', 'readthebill.rtb.views.rushed_bills', name="rushed_bills"),
    url(r'^endorsements/', 'django.views.generic.simple.direct_to_template', {'template': 'endorsements.html'}, name="endorsements"),
    url(r'^invite/', 'django.views.generic.simple.direct_to_template', {'template': 'invite.html'}, name="invite"),
    url(r'^call/(?P<id>\d+)/$', 'callingtool.views.call_legislator', name='call_legislator'),
    url(r'^call/', include('callingtool.urls')),
    url(r'^', include('mediasync.urls')),
    url(r'^$', 'readthebill.rtb.views.index', name="index"),
)
