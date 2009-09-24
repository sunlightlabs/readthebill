from django.conf.urls.defaults import *

urlpatterns = patterns('callingtool.views',

    url(r'^zip_rep/(?P<zipcode>\d+)/$', 'zip_rep'),
    url(r'^zip_direct/(?P<zipcode>\d*)/$', 'zip_direct'),
    url(r'^$', 'legislator_list', name='legislator_list'),
    url(r'^(?P<id>\d+)/$', 'call_legislator', name='call_legislator'),
    url(r'^state_reps/(?P<state>[A-Z]{2})/$', 'state_reps', name='state_reps'),
    url(r'^submit_call/(?P<id>\d+)/$', 'submit_call', name='submit_call'),
    url(r'^all_calls/$', 'all_calls', name='all_calls'),
    url(r'^delete_call/(?P<id>\d+)/$', 'delete_call', name='delete_call'),

)
