from django.conf.urls import url
from . import views

app_name = 'gestion'
urlpatterns=[
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^new/$', views.CreateView.as_view(), name='edit'),
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
    #url CAUSE
    url(r'^cause$', views.cause_list, name='cause_list'),
    url(r'^cause/(?P<pk>[0-9]+)/$', views.cause_detail, name='cause_detail'),
    url(r'^cause/new/$', views.cause_new, name='cause_new'),
    url(r'^cause/(?P<pk>[0-9]+)/edit/$', views.cause_edit, name='cause_edit'),
    #url MOUVEMENT
    url(r'^mouvement$', views.mouvement_list, name='mouvement_list'),
    url(r'^mouvement/(?P<pk>[0-9]+)/$', views.mouvement_detail, name='mouvement_detail'),
    url(r'^mouvement/new/$', views.mouvement_new, name='mouvement_new'),
    url(r'^mouvement/(?P<pk>[0-9]+)/edit/$', views.mouvement_edit, name='mouvement_edit'),
]
