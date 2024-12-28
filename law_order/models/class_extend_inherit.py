from odoo import api, fields, models, _
from datetime import datetime, date, timedelta



class InheritClass(models.Model):
    _name = "sale.order"
    _inherit = "sale.order"

    new_field = fields.Char(string="New Field")