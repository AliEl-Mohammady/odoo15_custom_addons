# -*- coding: utf-8 -*-
{
    'name': "OM Hospital Portal",

    'summary': """
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ali El-Mohamed",
    'website': "https://www.yourcompany.com",

    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['om_hospital','portal'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/om_hospital_portal_view.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'wb_portal/static/**/*',
        ],
    },

}