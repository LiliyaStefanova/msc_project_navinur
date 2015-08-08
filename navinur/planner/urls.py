__author__ = 'liliya'

from django.conf.urls import patterns, url
import navinur.routing

urlpatterns = patterns('navinur.planner.views',
                       url(r'^plan$', 'display_map'),
                       url(r'^get_route$', 'get_route'))
