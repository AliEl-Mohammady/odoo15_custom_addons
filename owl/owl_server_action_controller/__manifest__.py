# -*- coding: utf-8 -*-
{
    'name' : 'OWL Control Server Action',
    'version' : '1.0',
    'summary': '',
    'sequence': -1,
    'description': """Control Archive action view""",
    'category': 'OWL',
    'depends' : ['base', 'web'],
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/sale_order_inherit.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'owl_server_action_controller/static/src/components/**/*.js',
        ],
    },
}