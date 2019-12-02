#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   m_zhihu_example.py
@Time    :   2019/12/02 18:56:54
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''

import requests
from zhihu.m_zhihu import encrypt_data

_login_data = {
    "client_id": "c3cef7c66a1843f8b3a9e6a1e3160e20",
    "grant_type": "password",
    "source": "com.zhihu.web",
    "username": "",
    "password": "",
    "lang": "en",
    "ref_source": "homepage",
    "utm_source": ""
}


def login(captcha_type: str = "cn") -> bool:
    _login_data["lang"] = captcha_type
    data, session, headers = encrypt_data(login_data=_login_data)
    login_api = "https://www.zhihu.com/api/v3/oauth/sign_in"
    resp = session.post(login_api, data=data, headers=headers)
    print(resp.json())


login()
