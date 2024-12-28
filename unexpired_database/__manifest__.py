# -*- coding: utf-8 -*-
{
    'name': "unexpired_database",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose""",
    'author': "Ali El-Mohammady",
    'sequence': 2,
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    # 'excludes': ['om_odoo_inheritance'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'application': True,
}
