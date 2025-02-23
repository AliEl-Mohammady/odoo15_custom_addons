# -*- coding: utf-8 -*-
from odoo import models, fields, api,tools

class PosSaleOrder(models.Model):
    _name = 'pos.sale.order'
    _auto=False
    _description = 'Pos Sale Order'

    product_id = fields.Many2one(comodel_name='product.product',string='Product_id')
    partner_id = fields.Many2one(comodel_name='res.partner',string='Customer',)
    quantity = fields.Float(string='Quantity')
    price_unit = fields.Float(string='Price Unit',)
    date = fields.Date(string='Date')
    type = fields.Selection(string='Type',selection=[('sale', 'Sale'),('pos', 'Point of Sale'), ],)

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self._cr.execute("""
                    CREATE or REPLACE view %s as (
                        SELECT row_number() OVER () AS id, line.product_id, line.partner_id,
                        line.product_uom_qty as quantity,line.price_unit,line.date_order as date,line.type
                        FROM ( 
                        SELECT so.partner_id ,so.date_order,sol.product_id,sol.price_unit,sol.product_uom_qty,'sale' as type
                        FROM sale_order_line sol LEFT JOIN sale_order so ON (so.id=sol.order_id) WHERE so.state in ('done', 'sale')
                        UNION ALL
                        SELECT po.partner_id,po.date_order,pol.product_id,pol.price_unit,pol.qty,'pos' as type
                        FROM pos_order_line pol LEFT JOIN pos_order po ON (po.id=pol.order_id)
                        ) line
                    );
                """ % self._table)