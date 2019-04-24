# -*- encoding: utf-8 -*-
"""
version: 3.7
@time:  17:20
@author: xuanyue
@file: service.py
"""
from django import forms


class ServiceForm(forms.Form):
    name = forms.CharField(max_length=200, min_length=1, required=True,)
    description = forms.CharField(min_length=1, required=False,)
    parent = forms.IntegerField(required=True,)