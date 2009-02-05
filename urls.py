from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/gatekeeper/', include('gatekeeper.urls')),
    url(r'^admin/(.*)', admin.site.root),
    url(r'^partners/', 'readthebill.rtb.views.partners', name="partners"),
    url(r'^invite/', 'django.views.generic.simple.direct_to_template', {'template': 'invite.html'}, name="invite"),
    url(r'^$', 'readthebill.rtb.views.index', name="index"),
)