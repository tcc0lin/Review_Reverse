#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   m_baidu_index.py
@Time    :   2019/11/28 19:37:30
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''


def decrypt(t: str, e: str) -> str:
    n, i, a, result = list(t), list(e), {}, []
    ln = int(len(n)/2)
    start, end = n[ln:], n[:ln]
    a = dict(zip(end, start))
    return ''.join([a[j] for j in e])
