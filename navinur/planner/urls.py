__author__ = 'liliya'

from django.conf.urls import patterns, url

urlpatterns = patterns('navinur.planner.views',
                       url(r'^plan$', 'display_map'),
                       url(r'^get_route$', 'get_route'))
