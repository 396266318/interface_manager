# -*- encoding: utf-8 -*-
"""
version: 3.7
@time:  17:15
@author: xuanyue
@file: service.py
"""

from django.db import models

IS_ROOT = 0


class Service(models.Model):
    name = models.CharField("name", blank=False, default="", max_length=200)
    description = models.TextField("description", blank=True, default="")
    parent = models.IntegerField("父节点", blank=False, default=IS_ROOT)

    def __str__(self):
        return self.name
