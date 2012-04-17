from django.conf.urls.defaults import * 

urlpatterns = patterns('',
    url(r'^$', 'myproject.ujinga.views.home', name="home"),
)
