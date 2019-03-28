# -*- encoding: utf-8 -*-
"""
version: 3.7
@time:  17:15
@author: xuanyue
@file: service.py
"""

from django.db import models
from interface_app.models.base import Base

IS_ROOT = 0


class Service(models.Model, Base):
    name = models.CharField("name", blank=False, default="", max_length=200, verbose_name="名字")
    description = models.TextField("description", blank=True, default="", verbose_name="描述")
    parent = models.IntegerField("父节点", blank=False, default=IS_ROOT, verbose_name="父级")

    def __str__(self):
        return self.name
