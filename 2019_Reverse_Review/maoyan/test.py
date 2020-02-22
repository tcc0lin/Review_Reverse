#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2019/12/8 2:50:00
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''

from typing import (
    Dict,
    Any
)
import re
from io import BytesIO
from pathlib import Path
import requests
from lxml import etree
from fontTools.ttLib import TTFont
from maoyan.knn_font import Classify

_woff_path = Path(__file__).absolute().parent/"fonts"/"test.woff"
_board_url = "https://maoyan.com/board/1"
_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}
_classify = Classify()


def get_map(text: str) -> Dict[str, Any]:
    woff_url = re.findall(r"url\('(.*?\.woff)'\)", text)[0]
    font_url = f"http:{woff_url}"
    content = requests.get(font_url).content
    with open(_woff_path, 'wb') as f:
        f.write(content)
    font = TTFont(BytesIO(content))
    glyf_order = font.getGlyphOrder()[2:]
    info = []
    for g in glyf_order:
        coors = font['glyf'][g].coordinates
        coors = [_ for c in coors for _ in c]
        info.append(coors)
    map_li = map(lambda x: str(int(x)), _classify.knn_predict(info))
    uni_li = map(lambda x: x.lower().replace('uni', '&#x') + ';', glyf_order)
    return dict(zip(uni_li, map_li))


def get_board() -> None:
    text = requests.get(
            url=_board_url,
            headers=_headers
        ).text
    map_dict = get_map(text=text)
    for uni in map_dict.keys():
        text = text.replace(uni, map_dict[uni])
    html = etree.HTML(text)
    dd_li = html.xpath('//dl[@class="board-wrapper"]/dd')
    for dd in dd_li:
        p_li = dd.xpath(
            './div[@class="board-item-main"]//div[@class="movie-item-info"]/p')
        title = p_li[0].xpath('./a/@title')[0]
        star = p_li[1].xpath('./text()')[0]
        releasetime = p_li[2].xpath('./text()')[0]
        p_li = dd.xpath(
            './div[@class="board-item-main"]//div[@class="movie-item-number boxoffice"]/p')
        realtime_stont = ''.join(
            list(map(lambda x: x.strip(), p_li[0].xpath('.//text()'))))
        total_stont = ''.join(
            list(map(lambda x: x.strip(), p_li[1].xpath('.//text()'))))
        print(title)
        print(star)
        print(releasetime)
        print(realtime_stont)
        print(total_stont)
        print('-' * 50)


get_board()
