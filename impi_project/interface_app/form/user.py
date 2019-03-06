from django import forms


class UserForm(forms.Form):
    """用户名字段校验"""
    username = forms.CharField(
        max_length=20,
        min_length=3,
        required=True,
        error_messages={'required': '用户名不能为空'}
    )
    """密码字段校验"""
    password = forms.CharField(
        max_length=20,
        min_length=3,
        required=True,
        error_messages={'required': '密码不能为空'}
    )