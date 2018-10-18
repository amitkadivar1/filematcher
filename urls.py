from django.conf.urls.defaults import *
from django.conf.urls import patterns, url
urlpatterns = patterns(
    url(r'^files/', include('matcher.urls')),
    url(r'^admin/', include('django.contrib.admin.urls')),
)
