from django.conf.urls.defaults import *
from django.contrib import admin
from contact_form.forms import ContactForm

admin.autodiscover()

class RTBContactForm(ContactForm):
    from_email = "bounce@sunlightfoundation.com"
    recipient_list = ['jcarbaugh@sunlightfoundation.com','kmitchell@sunlightfoundation.com']
    subject = "[ReadTheBill.org] Contact"

urlpatterns = patterns('',
    url(r'^admin/gatekeeper/', include('gatekeeper.urls')),
    url(r'^admin/(.*)', admin.site.root),
    url(r'^contact/', include('contact_form.urls'), {"form_class": RTBContactForm, "fail_silently": False}),
    url(r'^partners/', 'readthebill.rtb.views.partners', name="partners"),
    url(r'^invite/', 'django.views.generic.simple.direct_to_template', {'template': 'invite.html'}, name="invite"),
    url(r'^$', 'readthebill.rtb.views.index', name="index"),
)