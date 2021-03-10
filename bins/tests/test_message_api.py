#!/usr/bin/env python
# !-*- coding:utf-8 -*-
# Create  : 2021/3/9 11:12 上午
# Author  : Z.Y.S
# File    : demo_custom_trigger.py
# Software: PyCharm
from xy.message_api import MessageApi

conn = MessageApi()


def test_get_templates():
    res = conn.get_templates()
    print(res)
    assert res["success"] is True


def test_send_mail_with_file():
    file1 = open('/Users/zhangyishu/项目/04_上汽集团/SRC项目计划v0.2.xmind', 'rb')
    file2 = open('/Users/zhangyishu/项目/04_上汽集团/SRC指标梳理-12.10.xmind', 'rb')
    res = conn.send_mail_with_file(tem_id=1, receiver_list="zhangyishu@qiniu.com", files=[file1, file2],
                                   name="zhangyishu",
                                   time="2021-03-09")
    assert res["success"] is True


def test_send_mail():
    res = conn.send_mail_with_file(tem_id=1, receiver_list="zhangyishu@qiniu.com", name="zhangyishu", time="2021-03-09")
    print(res)
    assert res["success"] is True


def test_get_sms_templates():
    res = conn.get_sms_templates()
    assert res["success"] is True


def test_get_email_templates():
    res = conn.get_email_templates()
    assert res["success"] is True


def test_send_sms():
    res = conn.send_sms("1338653753524228097", "17717456408", code="12345")
    assert res["success"] is True


def test_get_template_by_id():
    res = conn.get_template_by_id(1)
    assert res["success"] is True
