# -*- coding: utf-8 -*-
from pathlib import Path
import threading
import base64
import hashlib
import hmac
import json
import re
import time
from urllib.parse import urlencode
import execjs
import requests
from PIL import Image

encrypt_path = Path(__file__).absolute().parent/"encrypt.js"
login_data = {
    "client_id": "c3cef7c66a1843f8b3a9e6a1e3160e20",
    "grant_type": "password",
    "source": "com.zhihu.web",
    "username": "17610771895",
    "password": "linhanqiu",
    "lang": "en",
    "ref_source": "homepage",
    "utm_source": ""
}
session = requests.session()
session.headers.update({
    "accept-encoding": "gzip, deflate, br",
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
})


def _get_signature(timestamp: int): str:
    ha = hmac.new(
        b"d1b964811afb40118a12068ff74a12f4",
        digestmod=hashlib.sha1
    )
    grant_type = login_data["grant_type"]
    client_id = login_data["client_id"]
    source = login_data["source"]
    ha.update(
        bytes(
            (grant_type + client_id + source + str(timestamp)),
            "utf-8"
        )
    )
    return ha.hexdigest()


def _get_captcha(lang: str) -> str:
    if lang == "cn":
        api = "https://www.zhihu.com/api/v3/oauth/captcha?lang=cn"
    else:
        api = "https://www.zhihu.com/api/v3/oauth/captcha?lang=en"
    resp = session.get(api)
    show_captcha = re.search(r"true", resp.text)
    if show_captcha:
        put_resp = session.put(api)
        json_data = json.loads(put_resp.text)
        img_base64 = json_data["img_base64"].replace(r"\n", "")
        with open("./captcha.jpg", "wb") as f:
            f.write(base64.b64decode(img_base64))
        img = Image.open("./captcha.jpg")
        if lang == "cn":
            import matplotlib.pyplot as plt
            plt.imshow(img)
            print("点击所有倒立的汉字，在命令行中按回车提交")
            points = plt.ginput(7)
            capt = json.dumps({"img_size": [200, 44],
                               "input_points": [[i[0] / 2, i[1] / 2] for i in points]})
        else:
            img_thread = threading.Thread(target=img.show, daemon=True)
            img_thread.start()
            capt = input("请输入图片里的验证码：")
        # 这里必须先把参数 POST 验证码接口
        session.post(api, data={"input_text": capt})
        return capt
    return ""


def _get_xsrf():
    session.get("https://www.zhihu.com/", allow_redirects=False)
    for c in session.cookies:
        if c.name == "_xsrf":
            return c.value
    raise AssertionError("获取 xsrf 失败")


def _encrypt(form_data: dict):
    with open(encrypt_path) as f:
        js = execjs.compile(f.read())
        return js.call("Q", urlencode(form_data))


def login():
    timestamp = int(time.time() * 1000)
    login_data.update({
        "captcha": _get_captcha(login_data["lang"]),
        "timestamp": timestamp,
        "signature": _get_signature(timestamp)
    })
    headers = session.headers.copy()
    headers.update({
        "content-type": "application/x-www-form-urlencoded",
        "x-zse-83": "3_1.1",
        "x-xsrftoken": _get_xsrf()
    })
    data = _encrypt(login_data)
    login_api = "https://www.zhihu.com/api/v3/oauth/sign_in"
    resp = session.post(login_api, data=data, headers=headers)
    if "error" in resp.text:
        print(json.loads(resp.text)["error"])
    if check_login():
        print("登录成功")
        return True
    print("登录失败")
    return False


login(captcha_lang="cn")
