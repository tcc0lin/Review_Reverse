#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   md5.py
@Time    :   2019/11/22 16:47:29
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''
import hashlib


def md5crypto(string: str) -> str:
    hl = hashlib.md5()
    hl.update(string.encode(encoding='utf-8'))
    return hl.hexdigest()
