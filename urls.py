from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^api/ProcessEtxtRequest', 'views.api_process_incoming'),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
)
