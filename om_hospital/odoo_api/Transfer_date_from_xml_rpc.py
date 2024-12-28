import xmlrpc.client


url_db1 = "http://localhost:8030"
db_1 = 'om_hospital'
username_db_1 = 'admin'
password_db_1 = 'admin'


common_1 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_db1))
models_1 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_db1))
versiion_db1=common_1.version()
print("details",versiion_db1)

url_db2 = "http://localhost:8032"
db_2 = 'test'
username_db_2 = 'admin'
password_db_2 = 'admin'


common_2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url_db2))
models_2 = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url_db2))
versiion_2 = common_2.version()
print("details",versiion_2)



uid_db1 = common_1.authenticate(db_1, username_db_1, password_db_1, {})
uid_db2 = common_2.authenticate(db_2, username_db_2, password_db_2, {})
print("Uid",uid_db1)
print("Uid",uid_db2)

leeds=models_1.execute_kw(db_1, uid_db1, password_db_1, 'crm.lead', 'search_read', [[]], {'fields': ['name', 'id',],'limit':2})
print(leeds)
total_count=0
for leed in leeds :
	total_count+=1
	create_leads = models_2.execute_kw(db_2, uid_db2, password_db_2, 'crm.lead', 'create', [leed])
	print("create_partner",create_leads)
		
print("total_count",total_count)

