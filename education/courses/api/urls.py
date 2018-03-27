#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2018/3/27'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from django.urls import path, include
from rest_framework import routers

from . import views
from django.conf.urls import url


router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)

urlpatterns = [
    path(r'subjects/', views.SubjectListView.as_view(),
            name='subject_list'),
    path(r'subjects/(?P<pk>\d+)/',
            views.SubjectDetailView.as_view(),
            name='subject_detail'),

    # path(r'courses/(?P<pk>\d+)/enroll/',
    #      views.CourseEnrollView.as_view(),
    #      name='course_enroll'),

    path(r'', include(router.urls))

]