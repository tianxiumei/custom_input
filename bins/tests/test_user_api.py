#!/usr/bin/env python
# !-*- coding:utf-8 -*-
# Create  : 2021/3/9 11:12 上午
# Author  : Z.Y.S
# File    : demo_custom_trigger.py
# Software: PyCharm
from xy.user_api import UserAPI

xy_conn = UserAPI()


def test_get_tenants():
    res = xy_conn.get_tenants()
    print(res)
    assert res["success"] == True


def test_get_users_by_tenantid():
    res = xy_conn.get_users_by_tenantid(1364844406243201026)
    print(res)
    assert res["success"] is True


def test_get_user_info_by_id():
    res = xy_conn.get_user_info_by_id(1364844376841129986)
    print(res)
    assert res["success"] is True
