#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_m_nubia.py
@Time    :   2019/11/27 00:30:11
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''
import requests
from nubia.m_nubia import get_arg2


def test_m_nubia():
    headers = {
        "Cookie": get_arg2(),
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    response = requests.get('https://bbs.nubia.cn/', headers=headers)
    result = 1 if "努比亚官网" in response.text else 0
    assert result == 1
