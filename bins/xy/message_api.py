#!/usr/bin/env python
# !-*- coding:utf-8 -*-
# Create  : 2021/3/8 4:40 下午
import json

from xy.xy_api import XY_API
import mimetypes


class MessageApi(XY_API):
    def __init__(self):
        self.url = "http://116.228.13.134:31385/api/message-svc"
        super().__init__(self.url)

    def get_templates(self):
        # todo 获取租户下模板
        return self.get("/template?current=1&size=90000").json()

    def get_sms_templates(self):
        res = self.get_templates()
        if res["success"] == True:
            templates = res["data"]["records"]
            data = [record for record in templates if record["sendType"] == 2]
            res["data"] = data
            return res

    def get_email_templates(self):
        res = self.get_templates()
        if res["success"] is True:
            templates = res["data"]["records"]
            data = [record for record in templates if record["sendType"] == 1]
            res["data"] = data
            return res

    def send_sms(self, tem_id, receiver_list, **kwargs):
        # todo 发送短信
        header = {
            "Content-Type": "application/json"
        }
        payload = {
            "temId": tem_id,
            "receiverList": [receiver_list],
            "paramMap": {
                **kwargs
            }
        }
        payload = json.dumps(payload)
        return self.post("/templateMessage/sendSms", payload, header=header).json()

    def send_mail_with_file(self, tem_id, receiver_list, files=None, **kwargs):
        # todo 发送邮件(带或者不带附件)
        data = {'temId': tem_id,
                'receiverList': receiver_list}
        payload = dict(data, **kwargs)
        if files is None:
            return self.post("/templateMessage/sendMailWithFile", payload).json()
        f = []
        for file in files:
            file_name = file.name.split("/")[-1]
            content_type = mimetypes.guess_type(file.name)[0]
            f.append(('files', (file_name, file, content_type)))
        return self.post("/templateMessage/sendMailWithFile", payload, files=f).json()

    def get_template_by_id(self, id):
        return self.get(f"/template/{id}").json()
