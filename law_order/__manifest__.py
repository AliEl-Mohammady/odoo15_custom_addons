
{
    'name': "Law",
    'category': 'Law',
    'version': '1.0.0',
    'sequence': -11,
    'author': 'Ali Mohamed Mahmoud',
    'summary': "Law Management system",
    'description': "Law Management system",
    'depends': ['base','sale'],
    'data': ['views/lawyers_views.xml',
             'security/ir.model.access.csv',
             'views/customers_views.xml',
             'views/inherit_sales.xml',],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}