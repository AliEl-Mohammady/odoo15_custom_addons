# -*- coding: utf-8 -*-
{
    'name': "first_project",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose""",
    'author': "Ali Mohamed Mahmoud",
    'sequence': 2,
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'sale', 'mail','report_xlsx'],
    # 'excludes': ['om_odoo_inheritance'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/wizard_report_view.xml',
        'views/sale_order_first_project.xml',
        'reports/report.xml',
    ],
    'demo': [],
    'application': True,
}
