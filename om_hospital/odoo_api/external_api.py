					# python3.8 external_api.py

url = "http://localhost:8030"
db = 'om_hospital'
username = 'admin'
password = 'admin'

import xmlrpc.client

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version=common.version()
print("details",version)

uid = common.authenticate(db, username, password, {})
print("Uid",uid)

# check access rights
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
check_access_read=models.execute_kw(db, uid, password, 'res.partner', 'check_access_rights', ['read'], {'raise_exception': False})
print("check_access_read",check_access_read)

# search for records (search method)
partner_ids=models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]], {'offset': 2, 'limit': 5})
print("partners",partner_ids)

partners_count=models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])
print("partners_count",partners_count)

# read records (read method)
partner_records = models.execute_kw(db, uid, password, 'res.partner', 'read', [partner_ids])
print(len(partner_records))
partner_records_specific_field=models.execute_kw(db, uid, password, 'res.partner', 'read', [partner_ids], {'fields': ['name', 'id',]})
print(partner_records_specific_field)
	
# search read records (read method)
partner_records_search_read=models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['id','=',45]]], {'fields': ['name', 'id',],'limit': 5})
for rec in partner_records_search_read :
	print('search_read',rec)	

create_partner = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "Ali El Mohammady","phone":"01025893594"}])
print("create_partner",create_partner)

#update record (write method)
print("**********XML RPC update record***********")
models.execute_kw(db, uid, password, 'res.partner', 'write', [[create_partner], {'name': "3li El-mohamady","phone":"0100000000000"}])
partner_records=models.execute_kw(db, uid, password, 'res.partner', 'read', [create_partner], {'fields': ['name', 'phone','active']})
print(partner_records)
models.execute_kw(db, uid, password, 'res.partner', 'action_unarchive', [[create_partner]])
print(partner_records)

#delete record (unlink method)
print("**********XML RPC delete record***********")
models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[create_partner]])
partner_records=models.execute_kw(db, uid, password, 'res.partner', 'read', [create_partner], {'fields': ['name', 'phone',]})
print(partner_records)

