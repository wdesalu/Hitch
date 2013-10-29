from django.conf.urls import patterns, url

from hitch import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    # ex: /hitch/5/
    url(r'^(?P<hitch_driver_id>\d+)/$', views.detail, name='detail'),
    # ex: /hitch/5/results/
    url(r'^(?P<driver_id>\d+)/results/$', views.results, name='results'),
    # ex: /hitch/5/vote/
    url(r'^(?P<driver_id>\d+)/vote/$', views.vote, name='vote'),
)

