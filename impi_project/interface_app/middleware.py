import traceback
from django.utils.deprecation import MiddlewareMixin
from django.db import DatabaseError
from interface_app.my_exception import MyException
from interface_app.common import response_failed


class MyExceptionMiddleware(MiddlewareMixin):
    """请求进来"""
    def process_request(self, request):
        print("请求进来")

    """响应返回"""
    def process_response(self, request, response):
        print("响应返回")
        return response

    def process_exception(self, request, exception):
        print(traceback.print_exc())
        if isinstance(exception, MyException):
            print("操作错误")
            return response_failed(exception.message)

        elif isinstance(exception, DatabaseError):
            print("数据库错误")
            return response_failed("数据库错误")

        else:
            print("未知错误")
            return response_failed("未知错误")
