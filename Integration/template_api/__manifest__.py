# -*- coding: utf-8 -*-
{
    'name': "Api Template",

    'summary': """This template to handle api requests""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ali El-Mohammady",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/access_token.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
