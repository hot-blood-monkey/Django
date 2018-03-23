#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2018/3/21'
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

from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """异步发送邮件通知购买成功"""
    order = Order.objects.get(id=order_id)
    subject = 'Order nr . {}'.format(order.id)
    message = '亲爱的{},您已经成功下单。订单号为{}。'.format(order.first_name,order.id)
    mail_sent = send_mail(subject,message,'290322402@qq.com',[order.email])

    return mail_sent
