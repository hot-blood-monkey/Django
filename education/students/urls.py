#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2018/3/25'
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
from django.conf.urls import url
from django.urls import path
from django.views.decorators.cache import cache_page
from . import views


urlpatterns = [
    path(r'register/', views.StudentRegistrationView.as_view(),
         name='student_registration'),

    path(r'enroll-course/', views.StudentEnrollCourseView.as_view(),
         name='student_enroll_course'),

    url(r'^course/(?P<pk>\d+)/$',
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail'),

    url(r'^course/(?P<pk>\d+)/(?P<module_id>\d+)/$',
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail_module'),

]