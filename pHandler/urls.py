from django.conf.urls import patterns, include, url
from pHandler.views import *
# from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^', List.as_view(), name='phandler-list'),
                       )
