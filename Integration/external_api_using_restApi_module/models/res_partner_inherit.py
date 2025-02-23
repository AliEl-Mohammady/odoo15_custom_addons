# -*- coding: utf-8 -*-

from odoo import models, fields, api


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

        return kwargs

