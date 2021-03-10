#!/usr/bin/env python
# !-*- coding:utf-8 -*-
# Create  : 2021/3/9 11:23 上午
# Author  : Z.Y.S
from pdr_python_sdk.tools.mock_tools import mock_api_request

from message import Message


def test_get_all_templates():
    res = mock_api_request(Message, path="/custom/v1/demo_custom_trigger/message/templates")
    print(res[1])
    assert res[0] == 200


def test_get_sms_templates():
    res = mock_api_request(Message, path="/custom/v1/demo_custom_trigger/message/templates/sms")
    print(res[1])
    assert res[0] == 200


def test_get_email_templates():
    res = mock_api_request(Message, path="/custom/v1/demo_custom_trigger/message/templates/email")
    print(res[1])
    assert res[0] == 200


def test_send_sms():
    res = mock_api_request(Message, path="/custom/v1/demo_custom_trigger/message/send/sms",
                           param={"tem_id": "1338653753524228097", "receiver_list": '"17717456408","18121004328"',
                                  "code": "12345"})
    print(res[1])
    assert res[0] == 200


def test_send_email():
    res = mock_api_request(Message, path="/custom/v1/demo_custom_trigger/message/send/email",
                           param={"tem_id": "1", "receiver_list": "zhangyishu@qiniu.com", "name": "zhangyishu",
                                  "time": "2021-03-09"})
    print(res[1])
    assert res[0] == 200


def test_get_template_by_id():
    res = mock_api_request(Message, path="/custom/v1/demo_custom_trigger/message/templates/id",
                           param={"id": "1"})
    print(res[1])
    assert res[0] == 200
