from django.conf.urls import url
from . import views


app_name='account'
urlpatterns = [
    # post views
    url(r'^login/$', views.user_login, name='login'),
]