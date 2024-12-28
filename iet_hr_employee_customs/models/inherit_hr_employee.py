# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from dateutil.relativedelta import relativedelta


class HrEmployee(models.Model):
    _inherit = "hr.employee"


    custom_duration0_due0 = fields.Float(string='Duration Due', digits=(12, 3), help=" more than 5 Years",compute="_compute_custom_duration0_due0")
    amount_of_net_days = fields.Float(digits=(12, 5), help="Amount Of Net Days",compute="_compute_amount_of_net_days")

    @api.depends("name","end_work_date")
    def _compute_custom_duration0_due0(self):
        for rec in self:
            if rec.end_work_date:
                delta = relativedelta(rec.end_work_date, rec.contract_id.first_contract_date)
                print("delta.years",delta.years)
                print("delta.months",delta.months)
                print("delta.days",delta.days)
                days = delta.years * 365 + delta.days
                months = delta.years * 12 + delta.months
                years = delta.years + (delta.months / 12.0)
                print(rec.contract_id,rec.contract_id.first_contract_date,rec.contract_ids)
                rec.custom_duration0_due0 = delta.years*360+delta.months*30+delta.days-1800

    @api.depends("name","amount_of_net_days_less5","amount_of_net_days_after5")
    def _compute_amount_of_net_days(self):
        for rec in self:
                rec.amount_of_net_days =abs(rec.amount_of_net_days_less5-rec.amount_of_net_days_after5)
