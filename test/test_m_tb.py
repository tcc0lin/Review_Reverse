#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test_m_tb.py
@Time    :   2019/11/22 17:30:11
@Author  :   lateautumn4lin
@PythonVersion  :   3.7
'''
from tb.m_tb import get_sign
import pytest
import sys
print(sys.path)


def test_m_tb():
    assert get_sign(
        appKey="12574478",
        t="1574413784519",
        token="f8346f2bf8f4185ce0b5963a6c3f8599",
        data={"q": "鞋架", "sst": "1", "n": 20, "buying": "buyitnow", "m": "api4h5",
              "token4h5": "", "abtest": "35", "wlsort": "35", "page": 1}
    ) == "1dc8e43d5bb520d9f281af040aff10a4"
