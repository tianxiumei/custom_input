#!/usr/bin/env python
# !-*- coding:utf-8 -*-
# Create  : 2021/3/9 11:12 上午

import json
from unittest import TestCase

from xy.message_api import MessageApi

conn = MessageApi()


class TestMessageApi(TestCase):

    def test_get_templates(self):
        res = conn.get_templates()
        print(res)
        assert res["success"] is True

    def test_send_mail_with_file(self):
        file1 = open('/Users/zhangyishu/项目/04_上汽集团/SRC项目计划v0.2.xmind', 'rb')
        file2 = open('/Users/zhangyishu/项目/04_上汽集团/SRC指标梳理-12.10.xmind', 'rb')
        res = conn.send_mail_with_file(tem_id=1, receiver_list="zhangyishu@qiniu.com", files=[file1, file2],
                                       name="zhangyishu",
                                       time="2021-03-09")
        assert res["success"] is True

    def test_send_mail(self):
        values = {'alertLevel': '致命', 'eventName': 'test', 'eventDescription': 'te', 'eventStatus': '新建', 'eventSubject': 'count=0', 'eventTime': '2021-03-12 11:18:00', 'alertDescription': 'te', 'additionContents': [{'code': [{'code': '9999', '_time': '1615519080053'}]}, {'name': [{'name': 'hbacaien', '_time': '1615519080056'}]}], 'alertSourceType': '日志告警', 'phoenixHost': 'http://100.100.34.141:9999'}
        res = conn.send_mail_with_file(tem_id=1369985373148831746, receiver_list="zhangyishu@qiniu.com", **values)
        print(res)
        assert res["success"] is True

    def test_get_sms_templates(self):
        res = conn.get_sms_templates()
        assert res["success"] is True

    def test_get_email_templates(self):
        res = conn.get_email_templates()
        print(json.dumps(res).encode('utf-8'))
        assert res["success"] is True

    def test_send_sms(self):
        res = conn.send_sms("1338653753524228097", "17717456408, 18121004328", code="12345")
        assert res["success"] is True

    def test_get_template_by_id(self):
        res = conn.get_template_by_id(1)
        assert res["success"] is True

    def test_get_replace_field_by_id(self):
        res = conn.get_replace_field_by_id(1)
        print(res)
