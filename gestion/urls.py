from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.compte_list, name='compte_list'),
    url(r'^compte/(?P<pk>[0-9]+)/$', views.compte_detail, name='compte_detail'),
    url(r'^compte/new/$', views.compte_new, name='compte_new'),
    url(r'^compte/(?P<pk>[0-9]+)/edit/$', views.compte_edit, name='compte_edit'),
]
