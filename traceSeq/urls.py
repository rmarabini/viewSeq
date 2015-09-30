from django.conf.urls import patterns, url
from traceSeq import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^indexStruct/', views.indexStruct, name='index'),
)
#        url(r'^updateState/$', views.updateState, name='updateState'),
