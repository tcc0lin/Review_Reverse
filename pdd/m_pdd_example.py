#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   m_pdd_example.py
@Time    :   2019/12/18 18:59:40
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''

import re
import requests
import json

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "yangkeduo.com",
    "Upgrade-Insecure-Requests": "1",
    "Cookie": "api_uid=CiU+W135sAg7XwBFhLtfAg==; ua=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F79.0.3945.79%20Safari%2F537.36; _nano_fp=Xpd8n5EYn0Ean5XqnT_CS4kEsXdO51g4X2kTQecW; webp=1; pdd_user_id=4787727322403; pdd_user_uin=7UC3GHE35T33W2SU5TUPLUU3GU_GEXDA; PDDAccessToken=AFFFASIIHEH7QLAKMXT4FO42FE4LFKWJ7COWY3Z3366S23XINRIA1112347; JSESSIONID=791DFBCECCAE23DA89CAE1BFEBAB9086; rec_list_index=rec_list_index_2eFPGz",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}


def get_pdd_search_lst(search_name: str) -> None:
    with requests.get(
        url=f"http://yangkeduo.com/search_result.html?search_key={search_name}",
        headers=headers
    ) as response:
        data = re.findall(r"window.rawData=([\s\S]*?)</script>", response.text)
        if not data:
            raise Exception("extract json error")
        data = data[0].strip().strip(";")
        json_data = json.loads(data)["store"]["data"]["ssrListData"]
        msg_data = dict(json.loads(json_data["loadSearchResultTracking"]["req_params"]),
                        **{"flip": json_data["flip"]})

    headers["AccessToken"] = "AFFFASIIHEH7QLAKMXT4FO42FE4LFKWJ7COWY3Z3366S23XINRIA1112347"
    with requests.get(
        url=f"http://yangkeduo.com/proxy/api/search",
        headers=headers,
        params={
            "pdduid": "4787727322403",
            "source": "search",
            "search_met": "",
            "track_data": "refer_page_id,10169_1576665846887_tfHPiWnbtu",
            "list_id": msg_data["list_id"],
            "sort": "default",
            "filter": "",
            "q": search_name,
            "page": 2,
            "size": 50,
            "flip": msg_data["flip"],
            "anti_content": requests.get('http://localhost:8000/get_anti_content').json()["anti_result"]
        }
    ) as lst_response:
        print(len(lst_response.json()["items"]))


get_pdd_search_lst(search_name="书")
