

		# To run this file we use "python3 xml-rpc_odoo.py"

url = "http://localhost:8032"
db = 'school'
username = 'admin'
password = '5dcc2cd3bdfb3efae3ba28a38e00e128924d2b90'    	#we can use API key to connect to database insteed of password


import xmlrpc.client

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
versiion=common.version()
print("details",versiion)

uid = common.login(db, username, password)
print("Uid",uid)
