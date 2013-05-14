# -*- coding: utf-8 -*-  
from django.conf.urls import patterns, url
from .views import  login,singup,logout

urlpatterns = patterns("",
                        url(r'^$',login),
                        url(r'^login/$',login),
                        url(r'^singup/$',singup),
                        url(r'^logout/$',logout)
                       ) 