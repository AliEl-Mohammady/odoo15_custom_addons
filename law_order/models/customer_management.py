from odoo import api, fields, models, _
from odoo.exceptions import ValidationError,UserError
from datetime import datetime, date, timedelta
from dateutil import relativedelta
from lxml import etree


class CustomersManagement(models.Model):
    _name = "customers"
    _description = "Customers Management"
    _inherit = "lawyers"  # prototype inherit
    _inherits = {
        'lawyers': 'lawyer_id'}
    _rec_name = "age"

    user_id = fields.Many2one('res.partner', string="Name")
    age = fields.Integer(string="Age",store=True)
    age2 = fields.Integer(string="Age")
    number = fields.Integer()
    name = fields.Char(string="Name",related="lawyer_id.name",readonly=0)
    name_2 = fields.Char()
    description = fields.Char(string="Description")
    customers_id = fields.Many2one('lawyers', string="Age")
    lawyer_id = fields.Many2one('lawyers', string="Lawyers")
    company_id = fields.Many2one('res.company', string="Company")
    sequence_id=fields.Many2one('ir.sequence', string="Sequence")
    # env_search = fields.Char(string="Name")
    env_search_count = fields.Integer(string="Customer Count")
    so_id = fields.Many2one('sale.order', string="Age")
    notes=fields.Char(strin="Notes")




    # def print_record(self):
    #     customer = self.env['customers'].search([])
    #     self.env_search = customer.name

    @api.depends('so_id')
    def print_record(self):
        domain = [('partner_id', '=', self.user_id.id)]
        # count = self.env['sale.order'].search_count(domain)
        count = self.env['sale.order'].search(domain)
        self.env_search_count = count
        # for rec in count:
        #      print(rec.partner_id)
        # filtered = count.filtered('name')
        # print(filtered)
        check=self.search([])
        # check2=self.env['customers'].sudo().search([])
        # check2=self.env['customers'].with_context(active_test=True).search([])
        check2=self.env['customers'].with_user(self.user_id).search([])


    def create_method(self):
        record = {
            'name': 'Ali',
            'age': 23
        }
        record2 = {
            'name': 'Mahmoud',
            'age': 27
        }
        self.env['customers'].create([record2,record])

    @api.model
    def create(self, vals):
        vals['name_2'] = self.env['ir.sequence'].next_by_code('customer.sequence')
        return super(CustomersManagement, self).create(vals)

    def browse_method(self):
        # domain = [('partner_id', '=', self.user_id.id)]
        # count = self.env['sale.order'].search_count(domain)
        # browsed = self.env['customers'].browse(13)
        # browsed = self.env['customers'].browse(count)
        browsed = self.env['customers'].browse(self.lawyer_id.id)
        for rec in browsed :
            rec.description="goooood"
        print(browsed.name)

    @api.model
    def create(self, vals):
        browsed_lawyers = self.env['lawyers'].browse(vals.get('lawyer_id'))
        print(browsed_lawyers)
        for rec in browsed_lawyers:
            rec.price = 50
        print(vals)
        return super(CustomersManagement, self).create(vals)

    def mapped_method(self):
        searchable_lawyers = self.env['lawyers'].search([])
        # mapped_lawyers = searchable_lawyers.mapped('customers_id.name')
        # for rec in mapped_lawyers:
        #     print(rec)
        # mapped_lawyers = searchable_lawyers.mapped(lambda x: x.customers_id)
        mapped_lawyers = searchable_lawyers.mapped(lambda x: x.user.name)
        sorted_lawyers = searchable_lawyers.sorted(lambda x: x.age)
        # sorted_lawyers = searchable_lawyers.sorted('description')
        print(mapped_lawyers)
        # for rec in mapped_lawyers:
        #     print(rec.name)
        #
        # for rec in searchable_lawyers:
        #     print(rec.name)
        # print(sorted_lawyers)

    def name_get(self):
        # result = []
        # for rec in self:
        #     name =rec.description
        #     result.append((rec.id, name))
        # return result

        for rec in self:
            for rec in self:
                return [((rec.id, '%s (%s)' % (rec.age, rec.name)))]

    @api.model
    def default_get(self, fields):
        res = super(CustomersManagement, self).default_get(fields)
        res['age'] = 20
        return res


    def write(self, vals):
        vals['notes'] = self.env.user.name
        return super(CustomersManagement, self).write(vals)

    @api.returns('self', lambda x: x.id)
    def copy(self, default=None):
        if not default:
            default = {}
            default['name'] = self.name + "(copy)"
            default['name'] = _('%s(copy)' % self.name)
        return super(CustomersManagement, self).copy(default=default)

    @api.returns('self', lambda x: x.id)
    def copy(self, default=None):
        raise UserError(_("cant not be copied"))

    def unlink(self):
        for rec in self:
            if rec.age >= 30:
                raise ValidationError("can not be deleted")

    def unlink(self):
        lawyers_rec=self.mapped('lawyer_id')
        super(CustomersManagement,self).unlink()
        return lawyers_rec.unlink()

    #using create method to assign a field depend on other fields
    # def create(self, vals):
    #     for rec in vals:
    #         if "field_1" in rec and "field_2" not in rec:
    #             field_2 = self.env['module_name'].browse(vals['field_1']).uom_id.id
    #     return super(CustomersManagement, self).create(vals)

    @api.model
    def create(self, vals):
        if not vals['sequence_id']:
            if vals['lawyer_id'] and vals['user_id']:
                lawyer_id_rec = self.env['lawyers'].browse(vals['lawyer_id'])
                user_id_rec = self.env['res.partner'].browse(vals.get('user_id'))
                vals['sequence_id'] = self.env['ir.sequence'].sudo().create({
                    'name': lawyer_id_rec.name + '' + user_id_rec.name,
                    'padding': 5,
                    'prefix': "app",
                    'company_id': vals['company_id']
                }).id
            else:
                vals['sequence_id'] =self.env['ir.sequence'].sudo().browse(1).id
        return super(CustomersManagement, self).create(vals)

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(CustomersManagement, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,submenu=submenu)
        if view_type == 'form':
            doc = etree.XML(res['arch'])
            age_field = doc.xpath("//field[@name='age']")
            hoppy_field = doc.xpath("//field[@name='age']")
            number_field = doc.xpath("//field[@name='age']")
            if age_field:
                age_field[0].set("string", "New Age")
            res['arch'] = etree.tostring(doc, encoding='unicode')
            if hoppy_field:
                hoppy_field[0].addnext(etree.Element('label', {'string': 'Hoppy', 'name': 'hoppy'}))
            res['arch'] = etree.tostring(doc, encoding='unicode')
            if number_field:
                hoppy_field[0].addprevious(etree.Element('field',attrib={
                            'name': 'number',
                            'string': 'Number field from python file to xml ',
                            'invisible': '0',
                        }))
            res['arch'] = etree.tostring(doc, encoding='unicode')

        if view_type == 'tree':
            doc = etree.XML(res['arch'])
            age_field = doc.xpath("//field[@name='age']")
            if age_field:
                age_field[0].set("string", "New Age")
            res['arch'] = etree.tostring(doc, encoding='unicode')
            print("edxvd", res['arch'])
        return res

    def fields_get_method(self):
        field_get = self.fields_get(['lawyer_id'])
        for rec in self:
            print(">>>", self.fields_get([]))
            print(">>>", field_get)
            if field_get['lawyer_id']['company_dependent'] == False:
                rec.description = "Company dependent is False"
            else:
                rec.description = "Company dependent is True"

    def read_method(self):
        # records_search = self.search([])
        records_search = self.search([('id', '=', self.id)])
        records_read = records_search.read([])
        for rec in records_read:
            if rec['age']<1:
                rec['notes']="small"
            else:
                rec['notes'] = "big"
                print(rec['description'])
        records_search_read = records_search.search_read([])
        print(records_read)
        print(records_search_read)
        print(records_read[0]['id'])
