# -*- coding: utf-8 -*-
"""
author: Xuan
time: 2019-02-18 21:34
"""
import json
import logging
from django.http import JsonResponse


def response_json(success, message, data):
	"""json 响应 接收 success message data 参数, 进行解析, 返回Json 格式的响应"""
	result = dict()
	result['success'] = success
	result['message'] = message
	result['data'] = data
	
	return JsonResponse(result, safe=False)


def response_success(data={}):
	"""接收 data 参数 返回成功信息"""
	return response_json(True, "", data)


def response_failed(message="参数错误"):
	"""接收 message 参数返回失败信息"""
	return response_json(False, message, {})

logger = logging.getLogger(__name__)
