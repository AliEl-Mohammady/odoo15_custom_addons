from odoo import http
from odoo.http import request
import json
from odoo.addons.website.models.ir_http import sitemap_qs2dom
from odoo.addons.website_sale.controllers.main import WebsiteSale

class AppointementController(http.Controller):

    @http.route('/my/read_appointments', type='http', auth='public', website=True)
    def get_appointment(self):
        appointments = request.env["hospital.appointment"].search([])
        vals = {"appointments": appointments}
        return request.render('om_hospital_portal_odoomates.get_appointment_controller', vals)

    @http.route('/my/register_appointments', type='http', auth='public', website=True)
    def create_appointment(self):
        partners = request.env["hospital.patient"].sudo().search([])
        return request.render('om_hospital_portal_odoomates.register_appointments_controller',
                              {"appointment_ref": "HG0012", "partners": partners})

    @http.route('/my/register_appointments_form', type='http', auth='public', website=True, methods=['POST'], csrf=True)
    def create_appointment_form(self, **kw):
        # Access the form data submitted by the user
        appointment_ref = kw.get('appointment_ref')
        duration = kw.get('duration')
        partner_id = kw.get('partner_id')
        partner_rec = request.env["hospital.patient"].sudo().browse(partner_id)
        request.env['hospital.appointment'].create(
            {'ref': appointment_ref, 'duration': duration, "patient_id": partner_rec})
        return request.render('om_hospital_portal_odoomates.appointment_thanks', {})


class ShopInherit(WebsiteSale):

    def sitemap_shop(env, rule, qs):
        if not qs or qs.lower() in '/shop':
            yield {'loc': '/shop'}

        Category = env['product.public.category']
        dom = sitemap_qs2dom(qs, '/shop/category', Category._rec_name)
        dom += env['website'].get_current_website().website_domain()
        for cat in Category.search(dom):
            loc = '/shop/category/%s' % slug(cat)
            if not qs or qs.lower() in loc:
                yield {'loc': loc}

    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category"):category>''',
        '''/shop/category/<model("product.public.category"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True, sitemap=sitemap_shop)
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        res = super(ShopInherit, self).shop(page=page, category=category, search=search, min_price=min_price,
                                            max_price=max_price, ppg=ppg, **post)
        print(res)
        print(res.qcontext)
        # print(res.qcontext["page_name"])
        return res
