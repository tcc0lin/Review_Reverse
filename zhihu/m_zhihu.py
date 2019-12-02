#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   m_zhihu.py
@Time    :   2019/12/02 14:39:48
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''

import hmac
import time
import json
import base64
import re
import hashlib
from typing import (
    Dict,
    Tuple,
    Any
)
from pathlib import Path
import threading
from urllib.parse import urlencode
import requests
import execjs
from PIL import Image
import matplotlib.pyplot as plt


_login_data = ""
_captcha_url = "https://www.zhihu.com/api/v3/oauth/captcha?lang="
_encrypt_path = Path(__file__).absolute().parent/"encrypt.js"
_session = requests.Session()
_session.headers.update({
    "accept-encoding": "gzip, deflate, br",
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
})


def _get_signature(timestamp: int) -> str:
    ha = hmac.new(
        b"d1b964811afb40118a12068ff74a12f4",
        digestmod=hashlib.sha1
    )
    grant_type = _login_data["grant_type"]
    client_id = _login_data["client_id"]
    source = _login_data["source"]
    ha.update(
        bytes(
            (grant_type + client_id + source + str(timestamp)),
            "utf-8"
        )
    )
    return ha.hexdigest()


def _get_captcha(lang: str) -> str:
    api = f"{_captcha_url}cn" if lang == "cn" else f"{_captcha_url}en"
    resp = _session.get(api)
    show_captcha = re.search(r"true", resp.text)
    if show_captcha:
        put_resp = _session.put(api)
        json_data = json.loads(put_resp.text)
        img_base64 = json_data["img_base64"].replace(r"\n", "")
        with open("./captcha.jpg", "wb") as f:
            f.write(base64.b64decode(img_base64))
        img = Image.open("./captcha.jpg")
        if lang == "cn":
            plt.imshow(img)
            print(
                "Click all the inverted Chinese characters, Press enter on the command line to submit")
            points = plt.ginput(7)
            print(points)
            capt = json.dumps(
                {
                    "img_size": [200, 44],
                    "input_points": [[i[0] / 2, i[1] / 2] for i in points]
                }
            )
        else:
            img_thread = threading.Thread(target=img.show, daemon=True)
            img_thread.start()
            capt = input("input the Verification code:")
        _session.post(api, data={"input_text": capt})
        print(_session.cookies)
        return capt
    return ""


def _get_xsrf() -> str:
    _session.get("https://www.zhihu.com/", allow_redirects=False)
    for c in _session.cookies:
        if c.name == "_xsrf":
            return c.value
    raise AssertionError("get _xsrf params fail")


def _encrypt(form_data: Dict[str, str]) -> str:
    with open(_encrypt_path) as f:
        js = execjs.compile(f.read())
        return js.call("Q", urlencode(form_data))


def encrypt_data(login_data: Dict[str, str]) -> Tuple[Any]:
    global _login_data
    _login_data = login_data
    timestamp = int(time.time() * 1000)
    login_data.update({
        "captcha": _get_captcha(_login_data["lang"]),
        "timestamp": timestamp,
        "signature": _get_signature(timestamp)
    })
    headers = _session.headers.copy()
    headers.update({
        "content-type": "application/x-www-form-urlencoded",
        "x-zse-83": "3_1.1",
        "x-xsrftoken": _get_xsrf()
    })
    data = _encrypt(form_data=login_data)
    return data, _session, headers
