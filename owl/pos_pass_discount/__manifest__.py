# -*- coding: utf-8 -*-
{
    'name': "Pos Passcode For global Discount",

    'summary': """my first project using js to add a password when do a discount""",

    'description': """
       Pos js to pos_discount
    """,

    'author': "Ali El-Mohammady",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['pos_discount'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/pos_config_view.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_pass_discount/static/src/components/discount_pass.js'
        ]
    }
    ,
}
