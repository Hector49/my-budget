from django.conf.urls import url
from . import views

urlpatterns=[

    #url COMPTE
    url(r'^compte$', views.compte_list, name='compte_list'),
    url(r'^compte/(?P<pk>[0-9]+)/$', views.compte_detail, name='compte_detail'),
    url(r'^compte/new/$', views.compte_new, name='compte_new'),
    url(r'^compte/(?P<pk>[0-9]+)/edit/$', views.compte_edit, name='compte_edit'),
    #url POSTE
    url(r'^poste$', views.poste_list, name='poste_list'),
    url(r'^poste/(?P<pk>[0-9]+)/$', views.poste_detail, name='poste_detail'),
    url(r'^poste/new/$', views.poste_new, name='poste_new'),
    url(r'^poste/(?P<pk>[0-9]+)/edit/$', views.poste_edit, name='poste_edit'),
]
