from django.conf.urls import patterns, url

from hitch import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'client$', views.client, name='client'),
    url(r'/driver$', views.driver, name='driver'),
    url(r'/accept$', views.accept, name='accept'),

    # ex: /hitch/5/
    #url(r'^(?P<hitch_driver_id>\d+)/$', views.detail, name='detail'),
    
)

