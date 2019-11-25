#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   m_tb_example.py
@Time    :   2019/11/25 10:52:02
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''
import time
import json
import requests
from tb.m_tb import get_sign


def get_timestamp() -> int:
    millis = int(round(time.time() * 1000))
    return millis


def m_tb_example() -> None:
    ts = get_timestamp()
    appKey = "12574478"
    token = "723b90b162a25b20e8893878dd6fc11b"
    data = {
        "q": "鞋架",
        "sst": "1",
        "n": 20,
        "buying": "buyitnow",
        "m": "api4h5",
        "token4h5": "",
        "abtest": "44",
        "wlsort": "44",
        "page": 1
    }
    sign = get_sign(
        appKey=appKey,
        t=ts,
        token=token,
        data=data
    )
    with requests.get(
        url="https://acs.m.taobao.com/h5/mtop.taobao.wsearch.h5search/1.0/",
        headers={
            "Referer": "https://s.m.taobao.com/h5?q=%E9%9E%8B%E6%9E%B6",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
            "cookie": "cna=xzFiFsrV7nICAXt6Up3HKLZq; cookie2=1bcb7ca5a76780481ca4ed47788f7e46; t=04501bfd02f80387a432c63822ef12d3; _tb_token_=f3d31e5685333; ockeqeudmj=ppFA0T4%3D; munb=1813112602; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2Buiia%2Flzh1hmrxpw%3D; _w_app_lg=23; unb=1813112602; uc3=lg2=WqG3DMC9VAQiUQ%3D%3D&nk2=oiQyTXQm&id2=UonaVtgKd%2B0gDg%3D%3D&vt3=F8dByuQBIv%2FguevfaiM%3D; uc1=cookie14=UoTbmVY2i%2F7RcA%3D%3D&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&cookie21=V32FPkk%2FhoypzrZtAqoZbA%3D%3D; csg=f05277a6; lgc=%5Cu6797%5Cu97E9%5Cu79CB; ntm=0; cookie17=UonaVtgKd%2B0gDg%3D%3D; dnk=%5Cu6797%5Cu97E9%5Cu79CB; skt=0ddb940a43de093b; uc4=id4=0%40UOEw6Qk6Iks5HpdiZ39wT%2BBprLaq&nk4=0%40oCbqynVu30SuORvqWlHhPKM%3D; tracknick=%5Cu6797%5Cu97E9%5Cu79CB; _cc_=V32FPkk%2Fhw%3D%3D; _l_g_=Ug%3D%3D; sg=%E7%A7%8B2f; _nk_=%5Cu6797%5Cu97E9%5Cu79CB; cookie1=Bqbl1PQA9ioOXLoNO%2F%2BcChDL8mKymunmIfUh1MA5mV0%3D; enc=HEpmPLI1Yamon7ksmtNff2ciwHxUPqwd79qVT7SxHEs5yE7UO8oTDp8qf%2BE10J6rYLy5sGozFQUZxoB2CwFo%2Bw%3D%3D; x5sec=7b226d746f703b32223a223337383137653837393233316539373461356436383961363833336434616335434a2b493765344645493239744965677538546279774561444445344d544d784d5449324d4449374d513d3d227d; _m_h5_tk=723b90b162a25b20e8893878dd6fc11b_1574658113890; _m_h5_tk_enc=e5949dd78a44e353aae24db1315a6a58; l=dBaBezTnqWZ80iuxBOfahurza77TeIRb4sPzaNbMiICPOMCB5y0VWZpGpMT6CnGVHsiyR3oaseyTBeYBq_p7iVhJfxhD0RHqndC..; isg=BLe3WmhPplUSoCLVbYcGXJ4IRqsBfIveMjHSZQlk0wbtuNf6EUwbLnWZnhjmUGNW"
        },
        params={
            "jsv": "2.3.16",
            "appKey": appKey,
            "t": ts,
            "sign": sign,
            "api": "mtop.taobao.wsearch.h5search",
            "v": "1.0",
            "H5Request": "true",
            "ecode": "1",
            "AntiCreep": "true",
            "AntiFlool": "true",
            "type": "jsonp",
            "dataType": "jsonp",
            "callback": "mtopjsonp1",
            "data": json.dumps(data, separators=(",", ":"), ensure_ascii=False)
        },
        verify=False
    ) as response:
        print(response.text)


m_tb_example()
