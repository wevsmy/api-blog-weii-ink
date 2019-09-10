#!/usr/bin/env python
# coding:utf-8
"""
@Version: V1.0
@Author: willson
@License: Apache Licence
@Contact: willson.wu@goertek.com
@Site: goertek.com
@Software: PyCharm
@File: urls.py.py
@Time: 19-9-9 下午1:00
"""
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from api import views

# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register(r'users', views.UserViewSet, base_name='user')
router.register(r'groups', views.GroupViewSet, base_name='group')

# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
schema_view = get_swagger_view(title='Users API')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^docs/', schema_view, name="docs"),
    url(r'^', include(router.urls)),

    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^githubComments/$', views.GetIssuesComments.as_view()),
    url(r'^test/$', views.GetMessageView.as_view()),
]
