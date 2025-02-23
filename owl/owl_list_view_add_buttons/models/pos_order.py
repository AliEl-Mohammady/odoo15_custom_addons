# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosOrder(models.Model):
    _inherit = 'pos.order'

    def get_alert_call_js(self):
        return  "Add a new button to pos list view"