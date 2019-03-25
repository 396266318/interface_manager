# -*- encoding: utf-8 -*-
"""
version: 3.7
@time:  15:37
@author: xuanyue
@file: service_list_views.py
"""

import json
from interface_app import common
from interface_app.form.service import ServiceForm
from interface_app.models.service import Service, IS_ROOT
from interface_app.utils.service_utils import ServiceUtils

from django.views.generic import View
from interface_app.my_exception import MyException

# service 的列表获取和创建的接口


class ServiceListViews(View):

    def get(self, request, *args, **kwargs):
        """ 获取服务列表 """
        ret = ServiceUtils.get_service_tree_recursion(IS_ROOT)
        return common.response_success(ret)


    def post(self, request, *args, **kwargs):
        """ 创建服务 """
        body = request.body
        params = json.loads(body)
        form = ServiceForm(params)
        result = form.is_valid()
        if result:
            service = Service.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                parent=form.cleaned_data['parent']
            )
            if service:
                return common.response_success()
            else:
                raise MyException("创建失败")
        else:
            print(form.errors.as_json())
            return common.response_failed()