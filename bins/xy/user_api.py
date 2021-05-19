#!/usr/bin/env python
# !-*- coding:utf-8 -*-
# Create  : 2021/3/8 4:40 下午

from xy.xy_api import XY_API


class UserAPI(XY_API):
    def __init__(self):
        self.url = "http://127.0.0.1:8080/src-user-svc"
        super().__init__(self.url)

    def get_tenants(self):
        # todo 获取租户列表
        return self.get("/tenants/allTenant").json()

    def get_users_by_tenantid(self, tenantid):
        # todo 根据租户ID获取，租户下用户
        return self.get(f"/tenants/{tenantid}/users").json()

    def get_user_info_by_id(self, userid):
        return self.get(f"/users/selectByIds?ids={userid}").json()
