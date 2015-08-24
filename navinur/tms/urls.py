__author__ = 'liliya'


from django.conf.urls import patterns, url

urlpatterns = patterns('navinur.tms.views',
                       url(r'^$', 'root'),
                       # "/tms" calls root()
                       url(r'^(?P<version>[0-9.]+)$', 'service'),
                       url(r'^(?P<version>[0-9.]+)/'r'(?P<route_id>\d+)$', 'tile_map'),
                       url(r'^(?P<version>[0-9.]+)/' +
                           r'(?P<route_id>\d+)/(?P<zoom>\d+)/' +
                           r'(?P<x>\d+)/(?P<y>\d+)\.png$', 'tile'))
