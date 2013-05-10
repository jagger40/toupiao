# -*- coding: utf-8 -*-  
from django.conf.urls import patterns, include, url
from choice.views import index,auth,login,logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'choice.views.home', name='home'),
    # url(r'^choice/', include('choice.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index),
    url(r'^index/',index),
    url(r'^auth/$',auth),
    url(r'^auth/login/$',login),
    url(r'^auth/logout/$',logout),
    url(r'^auth/regist/$',auth),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^touke/',include('touke.urls'))
    
)


urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
    }),
)

urlpatterns += staticfiles_urlpatterns()


