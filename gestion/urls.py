from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.compte_list, name='compte_list'),
    url(r'^compte/(?P<pk>[0-9]+)/$', views.compte_detail, name='compte_detail'),
]
