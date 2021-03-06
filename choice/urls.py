# -*- coding: utf-8 -*-  
from django.conf.urls import patterns, include, url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from touke.views import index
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$',index),
    url(r'^index/',index),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^touke/',include('touke.urls')),
    url(r'^auth/',include('auth.urls')),
    
)


urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
    }),
)

urlpatterns += staticfiles_urlpatterns()


