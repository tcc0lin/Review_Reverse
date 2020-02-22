#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   m_nubia.py
@Time    :   2019/11/27 00:30:11
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''
import requests
import re
import base64
from urllib import parse

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}


def get_script_data() -> str:
    response = requests.get('https://bbs.nubia.cn/', headers=headers)
    arg1 = re.search("arg1='([^']+)'", response.text).group(1)
    return arg1


def unsbox(arg: str) -> str:
    _0x4b082b = [0xf, 0x23, 0x1d, 0x18, 0x21, 0x10, 0x1, 0x26, 0xa, 0x9, 0x13, 0x1f, 0x28, 0x1b, 0x16, 0x17, 0x19, 0xd,
                 0x6, 0xb, 0x27, 0x12, 0x14, 0x8, 0xe, 0x15, 0x20, 0x1a, 0x2, 0x1e, 0x7, 0x4, 0x11, 0x5, 0x3, 0x1c,
                 0x22, 0x25, 0xc, 0x24]
    _0x4da0dc = [''] * 40
    _0x12605e = ''
    for _0x20a7bf in range(0, len(arg)):
        _0x385ee3 = arg[_0x20a7bf]
        for _0x217721 in range(0, len(_0x4b082b)):
            if _0x4b082b[_0x217721] == _0x20a7bf + 0x1:
                _0x4da0dc[_0x217721] = _0x385ee3
    _0x12605e = ''.join(_0x4da0dc)
    return _0x12605e


def hexXor(_0x4e08d8: str, _0x23a392: str) -> str:
    _0x5a5d3b = ''
    _0xe89588 = 0x0
    while _0xe89588 < len(_0x23a392) and _0xe89588 < len(_0x4e08d8):
        _0x401af1 = int(_0x23a392[_0xe89588: _0xe89588 + 0x2], 16)
        _0x105f59 = int(_0x4e08d8[_0xe89588: _0xe89588 + 0x2], 16)
        _0x189e2c = hex(_0x401af1 ^ _0x105f59)
        if len(_0x189e2c) == 0x1:
            _0x189e2c = '\x30' + _0x189e2c
        _0x5a5d3b += _0x189e2c[2:]

        _0xe89588 += 0x2
    return _0x5a5d3b


def get_arg2() -> str:
    arg1 = get_script_data()
    key = '3000176000856006061501533003690027800375'
    _0x23a392 = unsbox(arg1)
    arg2 = 'acw_sc__v2=' + hexXor(key, _0x23a392)
    return arg2
