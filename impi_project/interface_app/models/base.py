# -*- encoding: utf-8 -*-
"""
version: 3.7
@time:  14:27
@author: xuanyue
@file: base.py
"""

import json
from django.core import serializers


class Base:
    def serializer_json(self, field):
        s = serializers.serialize('json', self, field=field)
        return s

    def serializer_dict(self, field):
        s = self.serializer_json(field)
        d = json.loads(s)
        return d
