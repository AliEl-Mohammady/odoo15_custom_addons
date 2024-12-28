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
        print(ctx)
        active_model = ctx.get('active_model')
        active_id = ctx.get('active_id')
        print(active_id)
        date_from = self.date_from
        date_to = self.date_to
        domain = [('date_order', '>=', date_from), ('date_order', '<=', date_to)]
        products = self.env['sale.order'].search(domain)
        products_list = []
        for prod in products:
            for line in prod.order_line:
                vals = {
                    'create_date': prod.date_order.date(),
                    'name': line.name,
                    'quantity': line.product_uom_qty,
                }
                products_list.append(vals)

        range_list = []
        count = list(range(len(products_list)))
        for unique_prod in products_list:
            for i in count:
                if unique_prod != products_list[i] and unique_prod['name'] == products_list[i]['name']:
                    unique_prod['quantity'] += products_list[i]['quantity']
                    range_list.append(unique_prod)
            if unique_prod not in range_list:
                range_list.append(unique_prod)

        max_quantity = []
        for range_prod in range_list:
            if range_prod['quantity'] not in max_quantity:
                max_quantity.append(range_prod['quantity'])

        max_quantity.sort(reverse=True)
        the_first_product = []
        the_second_product = []
        the_third_product = []
        for qty in range_list:
            if qty['quantity'] == max_quantity[0] and qty not in the_first_product:
                the_first_product.append(qty)
            elif qty['quantity'] == max_quantity[1] and qty not in the_second_product:
                the_second_product.append(qty)
            elif qty['quantity'] == max_quantity[2] and qty not in the_third_product:
                the_third_product.append(qty)

        data = {
            'form': self.read()[0],
            'user': self.env.user,
            'products_list': products_list,
            'the_first_product': the_first_product,
            'the_second_product': the_second_product,
            'the_third_product': the_third_product, }

        return self.env.ref('first_project.report_sale_orders_wizard').report_action(
            self.env[active_model].browse(active_id), data=data)

    def action_print_excel_reports(self):
        date_from = self.date_from
        date_to = self.date_to
        domain = [('date_order', '>=', date_from), ('date_order', '<=', date_to)]
        products = self.env['sale.order'].search(domain)
        products_list = []
        for prod in products:
            for line in prod.order_line:
                vals = {
                    'create_date': prod.create_date.date(),
                    'name': line.name,
                    'quantity': line.product_uom_qty,
                }
                products_list.append(vals)

        range_list = []
        count = list(range(len(products_list)))
        for unique_prod in products_list:
            for i in count:
                if unique_prod != products_list[i] and unique_prod['name'] == products_list[i]['name']:
                    unique_prod['quantity'] += products_list[i]['quantity']
                    range_list.append(unique_prod)
            if unique_prod not in range_list:
                range_list.append(unique_prod)

        max_quantity = []
        for range_prod in range_list:
            if range_prod['quantity'] not in max_quantity:
                max_quantity.append(range_prod['quantity'])

        max_quantity.sort(reverse=True)
        the_first_product = []
        the_second_product = []
        the_third_product = []
        for qty in range_list:
            if qty['quantity'] == max_quantity[0] and qty not in the_first_product:
                the_first_product.append(qty)
            elif qty['quantity'] == max_quantity[1] and qty not in the_second_product:
                the_second_product.append(qty)
            elif qty['quantity'] == max_quantity[2] and qty not in the_third_product:
                the_third_product.append(qty)

        data = {
            'form': self.read()[0],
            'products_list': products_list,
            'user': self.env.user.name,
            'company': self.env.company.name,
            'the_first_product': the_first_product,
            'the_second_product': the_second_product,
            'the_third_product': the_third_product, }
        return self.env.ref('first_project.report_patient_card_xls').report_action(self, data=data)
