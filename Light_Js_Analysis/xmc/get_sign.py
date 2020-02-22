import hashlib
import time
from typing import Dict
_cookie = "_ga=GA1.2.100938634.1582370964; _gid=GA1.2.927816681.1582370964; aliyungf_tc=AQAAABMm4j8LogsA5hre3Rf4QxA6bkWH; u_id=WEBabc27b4227ca5b27cb3e4fe61cf49d26d47eacdbefadefb28106cee6ef801cc4; account=l************%40163.com"


def get_md5(string: str) -> str:
    hl = hashlib.md5()
    hl.update(string.encode(encoding='utf-8'))
    return hl.hexdigest()


def get_p() -> str:
    index = _cookie.split(";")
    for i in index:
        if "u_id" in i:
            return i.split("u_id=")[-1]


def get_r() -> str:
    return str(int(round(time.time() * 1000)))


def get_g() -> str:
    p, r = get_p(), get_r()
    return get_md5(p+r)[7:], r


def get_s(d: Dict[str, str]) -> str:
    return "&".join(f"{k}={v}" for k, v in d.items())


def get_sign(formdata) -> str:
    g, r = get_g()
    s = get_s(d=formdata)
    return get_md5(r+s+g)


d = {
    "amount": "",
    "coinName": "USDT",
    "quantity": "0.1",
    "tradeType": "BUY"
}

