# -*- encoding: utf-8 -*-
"""
version: 3.7
@time:  16:55
@author: xuanyue
@file: task_list_views.py
"""
import json
from interface_app import common
from interface_app.form.task import TaskForm
from interface_app.models.task import Task, TaskInterface

from django.views.generic import View
from interface_app.my_exception import MyException
