# -*- encoding: utf-8 -*-
"""
version: 3.7
@time:  18:34
@author: xuanyue
@file: interface_utils.py
"""
import requests
import traceback

class InterfaceUtils:

    @classmethod
    def parse_parameter(cls, parameter):
        """
        form 形式的参数转成字典, 例如 [{"key": "a", "value": "a", "type": "string"}, {"key": "b", "value": "1", "type": "int"}]
        会转成字典: {"a": "a", "b": 1}
        :param parameter:
        :return:
        """
        ret = {}
        if not parameter:
            return ret
        for p in parameter:
            try:
                p_type = p.get("type", None)
                if p_type is None:
                    continue
                key = p.get("key", None)
                if key in None:
                    continue
                value = p.get("value", None)
                if value is None:
                    continue
                if "string" == p_type:
                    ret[key] = str(value)
                elif "int" == p_type:
                    ret[key] = int(value)
                elif "float" == p_type:
                    ret[key] = float(value)
                elif "bool" == p_type:
                    ret[key] = bool(value)
                else:
                    continue
            except Exception:
                continue
        return ret

    @classmethod
    def send_request(cls, url, method, header, parameter, parameter_type):
        ret = ''
        if "form" == parameter_type:  # 第一步, 把form 形式转换成字典, 如是json 则不需要转换
            parameter = cls.parse_parameter(parameter)

        try:
            if "GET" == method:
                ret = cls.__get_request(url, header, parameter)
            elif "POST" == method:
                ret = cls.__post_request(url, header, parameter, parameter_type)
            elif "DELETE" == method:
                ret = cls.__delete_request(url, header, parameter, parameter_type)
            elif "PUT" == method:
                ret = cls.__put_request(url, header, parameter, parameter_type)
            return ret
        except Exception:
            return traceback.format_exc()

    @classmethod
    def __set_header(cls, header, parameter_type):
        """
        头部信息校验
        :param header:
        :param parameter_type:
        :return:
        """
        if "json" == parameter_type:  # json 形式
            header["content-type"] = "application/json"
        else:  # form 形式
            header["content-type"] = "application/x-www-form-urlencoded"
        return header

    @classmethod
    def __get_request(cls, url, header, parameter):
        """
        get 请求, 数据都在url, 超时30s
        :param url:
        :param header:
        :param parameter:
        :return:
        """
        ret = requests.get(url, params=parameter, headers=header, timeout=30)
        return ret.text

    @classmethod
    def __post_request(cls, url, header, parameter, parameter_type):
        """
        post 请求 超时30s
        :param url:
        :param header:  字典
        :param parameter 字典
        :param parameter_type:
        :return:
        """
        header = cls.__set_header(header, parameter_type)
        if "json" == parameter_type:
            ret = requests.post(url, json=parameter, headers=header, timeout=30)
        else:
            ret = requests.post(url, data=parameter, headers=header, timeout=30)
        return ret.text

    @classmethod
    def __delete_request(cls, url, header, parameter, parameter_type):
        """
        delete 请求 超时30s
        :param url:
        :param header: 字典
        :param parameter: 字典
        :param parameter_type:
        :return:
        """
        header = cls.__set_header(header, parameter_type)
        if "json" == parameter_type:
            ret = requests.delete(url, json=parameter, headers=header, timeout=30)
        else:
            ret = requests.delete(url, data=parameter, headers=header, timeout=30)
        return ret.text

    @classmethod
    def __put_request(cls, url, header, parameter, parameter_type):
        """
        put 请求 超时30s
        :param url:
        :param header:
        :param parameter:
        :param parameter_type:
        :return:
        """
        header = cls.__set_header(header, parameter_type)
        if "json" == parameter_type:
            ret = requests.put(url, json=parameter, headers=header, timeout=30)
        else:
            ret = requests.put(url, data=parameter, headers=header, timeout=30)
        return ret.text