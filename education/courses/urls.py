#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2018/3/24'
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

from . import views

urlpatterns = [
    path(r'mine/',views.ManageCourseListView.as_view(), name='manage_course_list'),
    path(r'create/', views.CourseCreateView.as_view(), name='course_create'),
    url(r'^(?P<pk>\d+)/edit/$', views.CourseUpdateView.as_view(), name='course_edit'),
    path(r'(?<pk>\d+)/delete/',views.CourseDeleteView.as_view(),name='course_delete'),
    path(r'^(?P<pk>\d+)/module/', views.CourseModuleUpdateView.as_view(), name='course_module_update'),
    url(r'^module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/create/$',
            views.ContentCreateUpdateView.as_view(),
            name='module_content_create'),
    url(r'^module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/(?P<id>\d+)/$',
            views.ContentCreateUpdateView.as_view(),
            name='module_content_update'),

    url(r'^content/(?P<id>\d+)/delete/$', views.ContentDeleteView.as_view(),
                                            name='module_content_delete'),
    url(r'^module/(?P<module_id>\d+)/$',
        views.ModuleContentListView.as_view(),
        name='module_content_list'),

    url(r'^module/order/$', views.ModuleOrderView.as_view(), name='module_order'),
    url(r'^content/order/$', views.ContentOrderView.as_view(), name='content_order'),

    url(r'^subject/(?P<subject>[\w-]+)/$', views.CourseListView.as_view(),
                        name='course_list_subject'),
    url(r'^(?P<slug>[\w-]+)/$', views.CourseDetailView.as_view(),
                        name='course_detail'),

]