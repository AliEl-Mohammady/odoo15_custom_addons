# -*- coding: utf-8 -*-

{
    'name': "Hospital Management Portal",
    'category': 'Hospital',
    'version': '1.0.0',
    'sequence': -10,
    'author': 'Ali El-Mohammady',
    'summary': "Hospital Management system",
    'description': "Hospital Management system",
    'depends': ['website',"om_hospital","website_sale"],
    'data': [
        # 'security/ir.model.access.csv',
        'views/appointment_controller_portal.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
