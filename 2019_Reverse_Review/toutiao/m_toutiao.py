#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   m_toutiao.py
@Time    :   2019/11/28 17:02:45
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''
from pathlib import Path
from typing import Dict
import execjs


toutiao_dir = Path(__file__).absolute().parent
with open(toutiao_dir/'_get_as_cp_signature.js') as f:
    ctx = execjs.compile(f.read())


def get_as_cp_signature(ua: str, behot_time: int = 0) -> Dict[str, str]:
    params = {
        'category': '__all__',
        'tadrequire': 'true',
        'utm_source': 'toutiao',
        'widen': '1',
        '_signature': '',
        'as': '',
        'cp': '',
    }
    key = "min_behot_time" if not behot_time else "max_behot_time"
    params[key] = behot_time
    _as_cp = ctx.call('get_as_cp')
    params.update(_as_cp)
    _signature = ctx.call('get_signature', behot_time, ua)
    params['_signature'] = _signature
    return params
