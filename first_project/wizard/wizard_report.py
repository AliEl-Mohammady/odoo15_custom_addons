from odoo import api, fields, models, _

class WizardReport(models.TransientModel):
    _name = "wizard.report"
    _description = "Wizard Report"

    date_from = fields.Date(string='Date From', required=True, store=True, default=fields.Date.context_today)
    date_to = fields.Date(string='Date To', required=True, store=True, default=fields.Date.context_today)
    create_date = fields.Date(string="Creation Date", default=fields.Date.context_today)
    notes = fields.Text(string="Notes")

    def action_print_reports(self):
        ctx = self._context
        active_model = ctx.get('active_model')
        active_id = ctx.get('active_id')
        date_from = self.date_from
        date_to = self.date_to
        domain = [('order_id.date_order', '>=', date_from), ('order_id.date_order', '<=', date_to)]
        orders = self.env['sale.order.line'].search(domain)
        products = self.env['product.product'].search([])
        product_list = []
        product_list2 = []
        for prod in products:
            filter_sale_order = orders.filtered(lambda l: l.product_id == prod)
            print(filter_sale_order)
            for rec in filter_sale_order:
                product_list.append(rec.product_uom_qty)
            total_qty = sum(product_list)
            vals = {
                'id': prod.id,
                'name': prod.name,
                'quantity': total_qty,
            }
            product_list2.append(vals)

        product_list2.sort(key=lambda x: x['quantity'], reverse=True)
        data = {
            'form': self.read()[0],
            'user': self.env.user,
            'product_list2': product_list2,}
        print(product_list2)
        return self.env.ref('first_project.report_sale_orders_wizard').report_action(
            self.env[active_model].browse(active_id), data=data)

    def action_print_excel_reports(self):
        date_from = self.date_from
        date_to = self.date_to
        domain = [('order_id.date_order', '>=', date_from), ('order_id.date_order', '<=', date_to)]
        orders = self.env['sale.order.line'].search(domain)
        products = self.env['product.product'].search([])
        print(products)
        product_list = []
        product_list2 = []
        for prod in products:
            filter_sale_order = orders.filtered(lambda l: l.product_id == prod)
            for rec in filter_sale_order:
                product_list.append(rec.product_uom_qty)
            total_qty = sum(product_list)
            vals = {
                'id': prod.id,
                'name': prod.name,
                'quantity': total_qty,
            }
            product_list2.append(vals)

        product_list2.sort(key=lambda x: x['quantity'], reverse=True)
        data = {
            'form': self.read()[0],
            'user': self.env.user,
            'company': self.env.company.name,
            'product_list2': product_list2, }
        print(product_list2)
        return self.env.ref('first_project.report_sale_order_xls').report_action(self, data=data)
