# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import json


class resPartnerInherit(models.Model):
    _inherit = 'res.partner'

    def auth(self,url, db_name, db_login, db_password):
        url=url+'auth'
        payload={"params":{
             "login": db_login,
             "password": db_password,
             "db": db_name
        }}
        headers = {
            'content-type': "application/json",
        }
        response = requests.request("POST", url, data=json.dumps(payload),headers=headers)
        print(response)
        cookies = response.cookies
        if response.status_code == 200:
            response = json.loads(response.text)
            print(response)
            if "result" in response and response['result']['uid'] > 0:
                print(cookies)
                return {'cookies': cookies}
            else:
                return False
        else:
            return False

    def send_request_to_another_db(self, data):
        url="http://localhost:8030/"
        db_name="integration"
        db_login="admin"
        db_password="admin"
        authenticated=self.auth(url, db_name, db_login, db_password)
        if authenticated:
            url = url + "object/res.partner/create_partner"

            payload = {
                "params": {
                    "args": [],
                    "kwargs": data
                }
            }
            payload = json.dumps(payload)
            headers = {
                'content-type': "application/json",
            }
            response = requests.request("POST", url, data=payload, headers=headers, cookies=authenticated['cookies'])
            print("result response :> ", response.text)

    @api.model
    def create(self, vals):
        record=super().create(vals)
        self.send_request_to_another_db({"name":record.name, "phone":record.phone,"email":record.email})
        return record


    def get_records(self,args=[], **kwargs):
        first_10_records=self.env['res.partner'].search_read([],limit=10)
        records=list(first_10_records)
        return records
