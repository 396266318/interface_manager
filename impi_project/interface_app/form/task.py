# -*- encoding: utf-8 -*-
"""
version: 3.7
@time:  14:20
@author: xuanyue
@file: task.py
"""
from django import forms


class TaskForm(forms.Form):
    name = forms.CharField(max_length=200, min_length=1, required=True,)
    description = forms.CharField(max_length=500, min_length=1, required=False)
