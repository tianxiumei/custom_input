#!/usr/bin/env python
# !-*- coding:utf-8 -*-
# Create  : 2021/3/9 11:32 上午
from pdr_python_sdk.tools.mock_tools import mock_api_request

from tenants import Tenants


def test_get_tenants():
    res = mock_api_request(Tenants, path="/custom/v1/demo_custom_trigger/tenants")
    assert res[0] == 200


def test_get_tenants_user():
    res = mock_api_request(Tenants, path="/custom/v1/demo_custom_trigger/tenants/users",
                           param={"tenantid": "1356430095297376257"})
    assert res[0] == 200


def test_get_user_info():
    res = mock_api_request(Tenants, path="/custom/v1/demo_custom_trigger/tenants/users/info",
                           param={"userid": "1356436881656082434,1356505003491524609"})
    assert res[0] == 200
