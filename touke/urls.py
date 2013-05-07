from django.conf.urls import patterns, url

urlpatterns = patterns('touke.views',
    url(r'^$','findChoice'),
    url(r'^(?P<choice_id>\d+)/$','ChoiceDetail'),
)