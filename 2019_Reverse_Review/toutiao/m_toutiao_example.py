#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   m_toutiao_example.py
@Time    :   2019/11/28 16:54:52
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''

import time
import requests
from toutiao.m_toutiao import get_as_cp_signature

url = 'https://www.toutiao.com/api/pc/feed/'
ua = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 ' \
     '(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
headers = {
    'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'pragma': 'no-cache',
    'referer': 'https://www.toutiao.com/',
    'user-agent': ua,
    'x-requested-with': 'XMLHttpRequest'
}


def main() -> None:
    with requests.Session() as session:
        first_params = get_as_cp_signature(ua=ua)
        with session.get(url, params=first_params, headers=headers) as response:
            r_data = response.json()
            print(r_data["data"])
            next_hot_time = r_data['next']['max_behot_time']
        next_params = get_as_cp_signature(behot_time=next_hot_time, ua=ua)
        with session.get(url, params=next_params, headers=headers) as n_response:
            n_r_data = n_response.json()
            print(n_r_data["data"])


main()
