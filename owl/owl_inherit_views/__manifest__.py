# -*- coding: utf-8 -*-
{
    'name' : 'OWL Inherit View',
    'version' : '1.0',
    'summary': 'Todo List App',
    'sequence': -1,
    'description': """Add Buttons to res partner list view""",
    'category': 'OWL',
    'depends' : ['base', 'web','sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_inherit.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_qweb': [
            'owl_inherit_views/static/src/components/**/*.xml',
        ],
        'web.assets_backend': [
            'owl_inherit_views/static/src/components/**/*.js',
        ],
    },
}