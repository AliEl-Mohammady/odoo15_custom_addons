# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /home/ali/odoo/15e/custom_addons/cybrosys_portal(models.Model):
#     _name = '/home/ali/odoo/15e/custom_addons/cybrosys_portal./home/ali/odoo/15e/custom_addons/cybrosys_portal'
#     _description = '/home/ali/odoo/15e/custom_addons/cybrosys_portal./home/ali/odoo/15e/custom_addons/cybrosys_portal'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100