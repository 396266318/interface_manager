# -*- coding: utf-8 -*-
"""
author: Xuan
time: 2019-02-18 21:32
"""
import json
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from interface_app import common
from interface_app.form.user import UserForm

from django.views.generic import View
from interface_app.my_exception import MyException


class UserViews(View):



	def get(self, request, *args, **kwargs):
		user = request.user
		if user.is_authenticated:
			return common.response_success({"username": user.username, "id": user.id})
		else:
			raise MyException("用户未登录")



	def post(self, request, *args, **kwargs):
		"""单个服务"""
		body = request.body
		params = json.loads(body)
		form = UserForm(params)
		result = form.is_valid()

		if result:
			user = User.objects.create_user(
				username=form.cleaned_data["username"],
				password=form.changed_data["password"]
			)
			if user:
				login(request, user)
				session = request.session.session_key
				return common.response_success({"session": session})
			else:
				raise MyException("注册失败")
		else:
			print(form.errors.as_json())
			raise MyException()

	def put(self, request, *args, **kwargs):
		"""更新单个服务"""
		body = request.body
		params = json.loads(body)
		form = UserForm(params)
		result = form.is_valid()
		if result:
			user = authenticate(
				username=form.cleaned_data["username"],
				password=str(form.cleaned_data["password"])
			)
			if user:
				login(request, user)
				session = request.session.session_key
				return common.response_success({"session": session})
			else:
				raise MyException("登录失败")
		else:
			print(form.errors.as_json())
			raise MyException()
