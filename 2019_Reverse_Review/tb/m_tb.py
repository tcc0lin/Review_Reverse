#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   m_tb.py
@Time    :   2019/11/22 16:53:13
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''

from typing import (Dict, Union)
import json
from tools.md5 import md5crypto
from pprint import pprint as print


def get_sign(appKey: str, t: str, token: str, data: Dict[str, Union[str, int]]) -> str:
    print(f'{token}&{t}&{appKey}&{json.dumps(data,separators=(",",":"),ensure_ascii=False)}')
    return md5crypto(
        f'{token}&{t}&{appKey}&{json.dumps(data,separators=(",",":"),ensure_ascii=False)}'
    )