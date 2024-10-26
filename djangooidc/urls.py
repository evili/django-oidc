# coding: utf-8

from django.urls import re_path
from . import views

urlpatterns = [
                       re_path(r'^login$', views.openid, name='openid'),
                       re_path(r'^openid/(?P<op_name>.+)$', views.openid, name='openid_with_op_name'),
                       re_path(r'^callback/login/?$', views.authz_cb, name='openid_login_cb'),
                       re_path(r'^logout$', views.logout, name='logout'),
                       re_path(r'^callback/logout/?$', views.logout_cb, name='openid_logout_cb'),
            ]
