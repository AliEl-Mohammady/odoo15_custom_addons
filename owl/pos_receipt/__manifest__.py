# -*- coding: utf-8 -*-
{
    'name' : 'OWL POS Receipt',
    'version' : '1.0',
    'summary': 'POS Receipt',
    'sequence': -1,
    'description': """Receipt of Pos view""",
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
            'pos_receipt/static/src/components/**/*.xml',
        ],
        'web.assets_backend': [
            'pos_receipt/static/src/components/**/*.js',
        ],
    },
}