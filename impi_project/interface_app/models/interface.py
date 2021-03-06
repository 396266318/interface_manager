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
    name = models.CharField('name', blank=False, max_length=200, )
    description = models.TextField('description', default='', )

    host = models.CharField('host', default='', max_length=200, )
    url = models.CharField('url', blank=False, max_length=500, )
    method = models.CharField('method', blank=False, max_length=20, )
    headers = ObjectField('headers', default={}, )
    parameter = ObjectField('parameter', default={}, )
    parameter_type = models.CharField('parameter_type, json or form', default="json", max_length=20, )

    response = models.TextField('response', default="", )
    response_type = models.CharField('response_type, json or html', default="json", max_length=20, )

    service = models.ForeignKey(Service, blank=False, related_name='service_interfaces', on_delete=models.SET_DEFAULT,
                                default=0, )

    asserts = ObjectField('asserts', default=[], )

    def __str__(self):
        return self.name
