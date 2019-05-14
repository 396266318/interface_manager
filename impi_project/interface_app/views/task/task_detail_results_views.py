# -*- encoding: utf-8 -*-
"""
version: 3.7
@time:  18:19
@author: xuanyue
@file: task_detail_results_views.py
"""
import datetime
from django.forms.models import model_to_dict
from interface_app import common
from interface_app.models.task import Task, TaskInterface
from interface_app.models.result import TaskResult, InterfaceResult

from django.views.generic import View
from interface_app.my_exception import MyException

# task 接口的增删改查

class TaskDetailVersionViews(View):

    def get(self, request, pk, *args, **kwargs):
        """
        获取单个 任务版本列表
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        result = TaskResult.objects.filter(task_id=pk).order_by('-version')
        ret = []
        for i in result:
            tmp = dict()
            tmp['version'] = i.version
            tmp['task_id'] = i.task_id
            tmp['created'] = i.created.strftime("%Y-%m-%d %H:%M")
            tmp['id'] = i.id
            ret.append(tmp)
        return common.response_success(ret)

class TaskDetailVersionResultsViews(View):
    def get(self, request, pk, *args, **kwargs):
        """
        获取一个版本的结果列表
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        results = InterfaceResult.objects.filter(task_result_id=pk)
        ret = [model_to_dict(i) for i in results]
        return common.response_success(ret)