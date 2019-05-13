# -*- encoding: utf-8 -*-
"""
version: 3.7
@time:  16:00
@author: xuanyue
@file: task_utils.py
"""
from django.forms.models import model_to_dict
from interface_app.models.result import TaskResult, InterfaceResult


class TaskUtils:
    @classmethod
    def get_result_summary(cls, result_id):
        ret = {
            "succcess": 0,
            "failled": 0,
            "total": 0
        }
        if not result_id:
            return ret

        v = InterfaceResult.object.filter(task_result_id=result_id)
        for i in v:
            if i.success:
                ret["success"] += 1
            else:
                ret["failed"] += 1
        ret["total"] = ret["success"] + ret["failed"]
        return ret

    @classmethod
    def get_last_result_summary(cls, task_id):
        if not task_id:
            return cls.get_result_summary(None)
        result = cls.get_last_result(task_id)
        if not result:
            return cls.get_result_summary(None)
        else:
            ret = cls.get_result_summary(result.id)
            return ret

    @classmethod
    def get_last_result(cls, task_id):
        """得到最后结果"""
        if not task_id:
            return None
        results = TaskResult.objects.filter(task_id=task_id).order_by('-id')
        if 0 == len(results):
            return None
        else:
            return results[0]

    @classmethod
    def get_last_interface_result(cls, result_id, interface_id):
        if not result_id or not interface_id:
            return "无"
        v = InterfaceResult.objects.filter(task_result_id=result_id, interface_id=interface_id)
        if 0 == len(v):
            return "无"

        if v[0].success:
            return "成功"
        else:
            return "失败"
