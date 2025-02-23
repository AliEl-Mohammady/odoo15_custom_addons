# -*- coding: utf-8 -*-
{
    'name': "Pos Auth Discount",

    'summary': """my first project using js to add a password when do a discount""",

    'description': """
       Pos js to pos_discount
    """,

    'author': "Ali El-mohammady",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['pos_discount'],
    'data': [
        # 'security/ir.model.access.csv',
        'security/pos_discount_group.xml',
        # 'views/pos_config_view.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_auth_discount/static/src/js/discount_passcode.js'
        ]
    }
    ,
}
