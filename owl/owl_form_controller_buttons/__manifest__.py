# -*- coding: utf-8 -*-
{
    'name' : 'OWL Form Control Edit & Create Action',
    'version' : '1.0',
    'summary': '',
    'sequence': -1,
    'description': """Control Edit & Create Button""",
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
            'owl_form_controller_buttons/static/src/components/**/*.js',
        ],
    },
}