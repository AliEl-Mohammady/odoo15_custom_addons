# -*- coding: utf-8 -*-
{
    'name': "Receive API db",
    "version": "15.0.1",

    "author": "Ali El-Mohammady",
    "license": "AGPL-3",
    "website": "",

    'depends': ['base','odoo-rest-api-master',"sale"],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_inherit.xml'
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}
