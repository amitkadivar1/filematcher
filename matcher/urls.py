from django.conf.urls.defaults import *
from filematcher.matcher.models import *
from django.conf.urls import patterns, url
from . import views

#if use django 2 or upper version then replace url replace to path
#from django.urls import path
#like path('',views.nameofviews,name="anyname") 
info_dict = {
    'queryset': FileInstance.objects.all(),
}
urlpatterns = patterns(
    url('^$',views.index,name="index")
    url(r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    url(r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
)
