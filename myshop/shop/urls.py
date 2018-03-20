#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2018/3/18'
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


urlpatterns=[

    path(r'', views.product_list, name='product_list'),
    path(r'P<category_slug>[-\w]+/', views.product_list,
         name='product_list_by_category'),

    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail,
        name='product_detail'),

]