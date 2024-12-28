from odoo import api, fields, models, _
from datetime import datetime, date, timedelta
from dateutil import relativedelta


class LawyersManagement(models.Model):
    _name = "lawyers"
    _description = "Lawyers Management"
    _rec_name = 'name'  # by  default
    _order = 'name'  # by  default

    name = fields.Char(string="Name")
    new_field = fields.Char(string="New Field")
    field01 = fields.Text(string="Text Field")
    field02 = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Selection Field")
    field03 = fields.Boolean(string="Boolean Field")
    field04 = fields.Html(string="Html Field")
    field05 = fields.Image(string="Image Field")
    field06 = fields.Binary(string="Binary Field")
    age = fields.Integer(string="Age", compute="_compute_age")
    # birthday = fields.Date(string="Birthday", default=date.today())
    birthday = fields.Date(string="Birthday", default=fields.Date.context_today)
    time = fields.Datetime(string="Date Field", default=datetime.now())
    # time = fields.Datetime(string="Date Field", default=fields.Datetime.now)
    customer_id = fields.Many2one('customers', string="Customer")
    # customer_ids = fields.Many2many('customers', string="Customer")
    customers_ids = fields.One2many('customers', 'customers_id', string="Customer")
    user = fields.Many2one('res.users', string="User")
    description = fields.Char(string="Description")
    price = fields.Monetary(currency_field="currency_id", string="Price")
    currency_id = fields.Many2one('res.currency', string="Currency", related="company_id.currency_id")
    company_id = fields.Many2one('res.company', string="Company", related="user.company_id")
    reference = fields.Reference(selection=[('res.company', 'Company'), ('res.currency', 'Currency')],
                                 string="Reference Field")
    weight = fields.Float(string="Weight", digits="Discount")
    _sql_constraints = [
        ('unique_tag_name', 'unique (name)', 'This name already existing!'),
        ('check_weight', 'check(weight != 10)', 'weight of the patient must be more than 10!')]
    # appointment_count = fields.Integer(string="Count", compute="read_group_compute_method")
    appointment_count = fields.Integer(string="Count")

    def _compute_age(self):
        for rec in self:
            current_year = date.today()
            if rec.birthday:
                rec.age = current_year.year - rec.birthday.year
            else:
                rec.age = 1

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('age', operator, name), ('description', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)

    def read_group_method(self):
        domain = [('lawyer_id', '=', self.id)]
        searched_method = self.env['customers'].search(domain)
        print(searched_method)
        searched_count_method = self.env['customers'].search_count(domain)
        print(searched_count_method)
        read_group_method = self.env['customers'].read_group(domain=domain, fields=['lawyer_id'], groupby=['lawyer_id'])
        print(read_group_method)
        for rec in read_group_method:
            print(rec)
            customer_count = rec['lawyer_id_count']
            customer_id = rec['lawyer_id'][0]
            browsed = self.browse(customer_id)
            print(browsed)
            browsed.appointment_count = customer_count
            self = self - browsed
        self.appointment_count = 0
