from django.conf.urls import url
from . import views

app_name= 'CBV_app'

urlpatterns = [
    url(r'^$',views.Comp_List.as_view(),name='list'),
    url(r'^(?P<pk>[-\w]+)/$',views.Comp_Detail.as_view(),name='details'),
    url(r'^create',views.CreateV.as_view(),name='create'),
    url(r'^delete/(?P<pk>\d+)',views.DeleteV.as_view(),name='delete'),
    url(r'^update/(?P<pk>\d+)',views.UpdateV.as_view(),name='update')
]