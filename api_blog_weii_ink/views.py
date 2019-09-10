#!/usr/bin/env python
# coding:utf-8
"""
@Version: V1.0
@Author: willson
@License: Apache Licence
@Contact: willson.wu@goertek.com
@Site: goertek.com
@Software: PyCharm
@File: views.py.py
@Time: 19-9-9 下午4:52
"""

from django.http import HttpResponseRedirect,HttpResponse
from django.views import View


class homePage(View):

    def get(self, request):
        # 302 临时重定向
        # return HttpResponseRedirect('https://blog.weii.ink')
        html_content = '<a href="https://blog.weii.ink">home</a>'
        return HttpResponse(html_content)