# -*- coding: utf-8 -*-


from django.conf.urls import url
from django.contrib.auth.views import login, logout_then_login, logout, password_change_done, password_change, \
    password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from . import views



urlpatterns = [
    # post views
    # url(r'^login/$', views.user_login, name='login'),

    # login logout
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),

    # 修改密码
    url(r'^password-change/$', password_change, name='password_change'),
    url(r'^password-change/done/$', password_change_done, name='password_change_done'),

    #  重置密码reset password
    ## restore password urls
    url(r'^password-reset/$',
        password_reset,
        name='password_reset'),
    url(r'^password-reset/done/$',
        password_reset_done,
        name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^password-reset/complete/$',
        password_reset_complete,
        name='password_reset_complete'),

    #dashboard 的 view
    url(r'^$', views.dashboard, name='dashboard'),

    #用户注册
    url(r'^register/$',views.register,name='register'),
    #path(r'register/',views.register,name='register'),

    #编辑他们的pfofile
    url(r'^edit/$', views.edit, name='edit'),


]
