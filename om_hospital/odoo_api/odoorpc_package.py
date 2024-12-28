            # https://pypi.org/project/OdooRPC/    :link for getting more information about rpc
            # python3.8 odoorpc_package.py         :to run file



import odoorpc

# Prepare the connection to the server
self = odoorpc.ODOO('localhost', port=8030)
# 
# Check available databases
print(self.db.list())

# Login
self.login('om_hospital', 'admin', 'admin')

# Current user
user = self.env.user
print(user.name)            # name of the user connected
print(user.company_id.name) # the name of its company

# # Simple 'raw' query
user_data = self.execute('res.users', 'read', [user.id])
# print(user_data)

# Use all methods of a model
if 'crm.lead' in self.env:
    Order = self.env['crm.lead'].search([],limit=2)
    for order in self.env['crm.lead'].browse(Order):
        print(order.name)

    leads=self.env['crm.lead'].create({'name':'Ali from odoorpc','email_from':'ali@gmail.com'})
    print(leads)
    lead=self.env['crm.lead'].browse(leads).write({'priority':'2'})
    print(lead)
    leads=self.env['crm.lead'].browse(leads).unlink()
    print(leads)

