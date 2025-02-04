__author__ = 'liliya'

from django.conf.urls import patterns, url

urlpatterns = patterns('navinur.planner.views',
                       url(r'^index/(?P<route_id>\d+)$', 'display_map'),
                       url(r'^calc_route$', 'calc_route'),
                       url(r'^display_route/(?P<route_id>\d+)$', 'display_route'),
                       url(r'^existing_routes$', 'existing_routes'))
