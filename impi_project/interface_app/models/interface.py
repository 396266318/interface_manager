# -*- encoding: utf-8 -*-
"""
version: 3.7
@time:  14:37
@author: xuanyue
@file: interface.py
"""
from django.db import models
from interface_app.models.service import Service
from interface_app.models.base import Base
from interface_app.fields.model.object_field import ObjectField


class Interface(models.Model, Base):
    name = models.CharField('name', blank=False, max_length=200, verbose_name="名称")
    description = models.TextField('description', default='', verbose_name="描述")

    host = models.CharField('host', default='', max_length=200, verbose_name="域名")
    url = models.CharField('url', blank=False, max_length=500, verbose_name="url")
    method = models.CharField('method', blank=False, max_length=20, verbose_name="方法")
    headers = ObjectField('headers', default={}, verbose_name="头部信息")
    parameter = ObjectField('parameter', default={}, verbose_name="参数")
    parameter_type = models.CharField('parameter_type, json or form', default="json", max_length=20, verbose_name="参数类型")

    response = models.TextField('response', default="", verbose_name="响应")
    response_type = models.CharField('response_type, json or html', default="json", max_length=20, verbose_name="响应类型")

    service = models.ForeignKey(Service, blank=False, related_name='service_interfaces', on_delete=models.SET_DEFAULT,
                                default=0, verbose_name="服务")

    asserts = ObjectField('asserts', default=[], verbose_name="断言")

    def __str__(self):
        return self.name
