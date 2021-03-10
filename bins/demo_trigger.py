import sys
import os
import logging
import json
import subprocess
import os
import sys

# add library to python path , don't forget it

lib_name = 'libs'
sys.path.insert(0, os.path.sep.join([os.path.dirname(os.path.abspath(__file__)), lib_name]))

from pdr_python_sdk.trigger_action.on_demand_trigger_action import OnDemandTriggerAction
from pdr_python_sdk.on_demand_action import run
from xy.message_api import MessageApi
from xy.user_api import UserAPI
from jsonpath import jsonpath


class DemoExample(OnDemandTriggerAction):

    def do_handle_init(self, packet):
        self.mess_conn = MessageApi()
        self.user_conn = UserAPI()

    def do_handle_events(self, events):
        length = len(events)
        logging.info(events)
        event_name = ""
        event_display_id = ""
        params = {}
        logging.info("event length = {0}".format(length))
        if length > 0:
            event_name = events[0].eventName
            event_display_id = events[0].eventDisplayId
            # 前端传过来的字段在params中
            params = events[0].params

        content = "from hello trigger: eventLength={0}, event_name={1}, " \
                  "event_display_id={2}, params={3}".format(length, event_name, event_display_id, params)

        return content

    def notice_src(self, user_id, tem_id):
        # todo 从前端传入的参数，得到发送类型，通过用户ID，获取用户的邮箱和手机号，通过模板ID，发送消息到对应地址
        user_info = self.user_conn.get_user_info_by_id(user_id)
        email = []
        phone = []
        for data in jsonpath(user_info, "data[*].email"):
            email.append(f'"{data}"')
        for data in jsonpath(user_info, "data[*].phone"):
            phone.append(f'"{data}"')
        email = ",".join(email)
        phone = ",".join(phone)
        self.mess_conn.send_mail_with_file(tem_id, email, files="", addparams1="", addparams2="")
        self.mess_conn.send_sms(tem_id, phone, addparams1="", addparams2="")


if __name__ == '__main__':
    # p = subprocess.Popen(' list', stdout=subprocess.PIPE, shell=True)
    # p.stderr.readlines()
    run(DemoExample, sys.argv, sys.stdin.buffer, sys.stdout.buffer)
