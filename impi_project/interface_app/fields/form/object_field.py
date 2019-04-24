# -*- encoding: utf-8 -*-
"""
version: 3.7
@time:  13:46
@author: xuanyue
@file: object_field.py
"""
import json
from django import forms


class ObjectField(forms.Field):
    def __init__(self, *args, **kwargs):
        super(ObjectField, self).__init__(*args, **kwargs)


    def to_python(self, value):
        """数据从model 读进来时进行处理"""
        if value is None:
            return dict()
        if isinstance(value, dict) or isinstance(value, list):
            return value
        try:
            ret = json.loads(value)
        except Exception:
            return dict()
        else:
            return ret

    def validate(self, value):
        """数据从前端请求进来时进行数据校验"""
        if self.required:
            if not isinstance(value, dict) or not isinstance(value, list):
                raise forms.ValidationError("格式正确")
        else:
            return self.to_python(value)
