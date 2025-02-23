# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import json

class resPartnerInherit(models.Model):
    _inherit = 'res.partner'


    def create_partner(self, args=[], **kwargs):
        self = self.sudo()   #Using sudo to pass if access found

        # parameters validations
        if not kwargs['name'] or not isinstance(kwargs['name'], str):   #isinstance  to check the type of the parameter
            return "not supported type for name"
        if not kwargs['email'] or not isinstance(kwargs['email'], str):
            return "not supported type for email"
        if not kwargs['phone'] or not isinstance(kwargs['phone'], str):
            return "not supported type for phone"

        # fill data
        vals = {}
        vals['name'] = kwargs['name']
        vals['email'] = kwargs['email']
        vals['phone'] = kwargs['phone']
        print("hello from api file")
        created = self.env['res.partner'].create(vals)
        kwargs['id'] = created.id
        print(kwargs)
        return kwargs

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


    def pull_contacts(self):
        url="http://localhost:8030/"
        db_name="owl_eman"
        db_login="admin"
        db_password="admin"
        authenticated=self.auth(url, db_name, db_login, db_password)
        print(authenticated)
        if authenticated :
            url = url + "object/res.partner/get_records"
            payload = {
                "params": {
                    "args": [],
                    "kwargs": {}
                }
            }
            payload = json.dumps(payload)
            headers = {
                'content-type': "application/json",
            }
            response = requests.request("POST", url, data=payload, headers=headers, cookies=authenticated['cookies'])
            # print("result response :> ", response.json())
            response_data = response.json()  # Parse the JSON response
            result = response_data.get('result')  # Extract the 'result' part
            # print(result)
            for record in result:
                self.env["res.partner"].create(record)
                print("partner created successfully")




