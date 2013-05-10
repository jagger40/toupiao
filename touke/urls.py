# -*- coding: utf-8 -*-  
from django.conf.urls import patterns, url

urlpatterns = patterns('touke.views',
    url(r'^$','findChoice'),
    url(r'^(?P<poll_id>\d+)/$','PollDetail'),
    url(r'^(?P<member_id>\d+)/home/$','home')
)

#API接口
urlpatterns += patterns('touke.views',
    url(r'^api/(?P<poll_id>\d+)/vote/$','vote'),
)