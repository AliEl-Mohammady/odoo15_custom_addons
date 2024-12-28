
from odoo import models, fields, api
from odoo.addons.sale.models.sale_order import SaleOrder as OdooSaleOrder


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    confirmed_user_id = fields.Many2one('res.users', string="Confirmed User", readonly=True)

    def action_confirm(self):
        super(SaleOrder,self).action_confirm()   #inherit function
        self.confirmed_user_id = self.env.user.id

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['so_confirmed_user_id'] = self.confirmed_user_id.id
        return invoice_vals

    # To override to inherited function
    def unlink(self):
        print("override to a function on odoo")
        return super(OdooSaleOrder,self).unlink()
#     OR
# def unlink(self):
#     return super(OdooSaleOrder,self).unlink()
# OdooSaleOrder.unlink=unlink

    def wizard_report(self):
        pass
