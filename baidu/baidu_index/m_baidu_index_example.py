#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   m_baidu_index_example.py
@Time    :   2019/11/28 19:38:00
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''

import time
import requests
from baidu.baidu_index.m_baidu_index import decrypt

COOKIES = 'BAIDUID=8759768F974CE3E6C2884260097331A4:FG=1; PSTM=1574683224; H_PS_PSSID=1445_21116_29567_29220; BIDUPSID=43233656E2011B10D268D7B02D7A956A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=2; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1574939615; BDUSS=hWWDJ0Z01VOWZINGdPaWRkTUotYmR4WlRhcEhJNTVDQzA3SUpDNzBSWHRPQWRlRVFBQUFBJCQAAAAAAAAAAAEAAAA3VXuxu6rPxNPQxMzGpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO2r313tq99daE; CHKFORREG=f47c79690c889b9fe3bb335ced026f76; bdindexid=j4g6p93elqe6o7phocmmfn53o2; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1574940479'
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Cookie': COOKIES,
    'DNT': '1',
    'Host': 'zhishu.baidu.com',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'zhishu.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
session = requests.Session()
session.headers.update(headers)


def get_ptbk(uniqid: str) -> str:
    with session.get(
        url=f"http://index.baidu.com/Interface/ptbk?uniqid={uniqid}"
    ) as response:
        ptbk = response.json()["data"]
        return ptbk


def get_index_data(keyword: str, start: str, end: str) -> str:
    with session.get(
        url=f"http://index.baidu.com/api/SearchApi/index?word={keyword}&area=0&startDate={start}&endDate={end}"
    ) as response:
        data = response.json()["data"]
        all_data = data["userIndexes"][0]["all"]["data"]
        uniqid = data["uniqid"]
        ptbk = get_ptbk(uniqid)
        result = decrypt(ptbk, all_data).split(',')
        return result


data = get_index_data(
    keyword="Python",
    start='2019-11-01',
    end='2019-11-28'
)
print(data)
