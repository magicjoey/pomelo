#!/usr/bin/env python
# encoding: utf-8
"""
    @author: Magic Joey
    @contact: outlierw@gmail.com
    @site: http://underestimated.me
    @project: mystery
    @description:
    @version: 2016-08-01 08:19,urls V1.0 
"""
from django.conf.urls import url
from front import views

urlpatterns = [
    url(r'^index_bak', views.index_bak),
    url(r'^index', views.index),
    url(r'^service', views.service),
    url(r'^element', views.element),
    url(r'^contact', views.contact),
    url(r'^portfolio', views.portfolio),
    url(r'^', views.index),
]
