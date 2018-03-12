#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2018/3/10'
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
from . import views

urlpatterns = [
    url(r'^create/$',views.image_create, name='create'),

    # 展示图片
    url(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.image_detail, name='detail'),

    url(r'^like/$', views.image_like, name='like'),

    url(r'^$', views.image_list, name='list'),
]