# -*- coding: utf-8 -*-
{
    'name' : 'OWL POS Add Button control Bar',
    'version' : '1.0',
    'summary': 'POS Add Button Control Bar',
    'sequence': -1,
    'description': """Add Buttons to Pos view""",
    'category': 'OWL',
    'depends' : ['base', 'web','point_of_sale'],
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/sale_order_inherit.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_qweb': [
            'pos_add_button_basic_view/static/src/components/**/*.xml',
        ],
        'web.assets_backend': [
            'pos_add_button_basic_view/static/src/components/**/*.js',
        ],
    },
}