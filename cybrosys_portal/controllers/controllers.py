# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class cybrosysPortal(http.Controller):
    @http.route('/my/sales_orders', auth='public',type='http',website=True)
    def get_date(self, **kw):
        sale_orders=request.env["sale.order"].search([])
        vals={"sale_orders":sale_orders}
        return request.render("cybrosys_portal.portal_my_page",vals)


    # @http.route('//home/ali/odoo/15e/custom_addons/cybrosys_portal//home/ali/odoo/15e/custom_addons/cybrosys_portal/objects', auth='public')
    # def list(self, **kw):
    #     return http.request.render('/home/ali/odoo/15e/custom_addons/cybrosys_portal.listing', {
    #         'root': '//home/ali/odoo/15e/custom_addons/cybrosys_portal//home/ali/odoo/15e/custom_addons/cybrosys_portal',
    #         'objects': http.request.env['/home/ali/odoo/15e/custom_addons/cybrosys_portal./home/ali/odoo/15e/custom_addons/cybrosys_portal'].search([]),
    #     })
    #
    # @http.route('//home/ali/odoo/15e/custom_addons/cybrosys_portal//home/ali/odoo/15e/custom_addons/cybrosys_portal/objects/<model("/home/ali/odoo/15e/custom_addons/cybrosys_portal./home/ali/odoo/15e/custom_addons/cybrosys_portal"):obj>', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('/home/ali/odoo/15e/custom_addons/cybrosys_portal.object', {
    #         'object': obj
    #     })
