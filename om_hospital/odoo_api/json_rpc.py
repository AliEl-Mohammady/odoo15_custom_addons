import json
import random
import urllib.request

HOST = 'localhost'
PORT = 8030
DB = 'om_hospital'
USER = 'admin'
PASS = 'admin'

def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": random.randint(0, 1000000000),
    }
    req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
        "Content-Type":"application/json",
    })
    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get("error"):
        raise Exception(reply["error"])
    return reply["result"]

def call(url, service, method, *args):
    return json_rpc(url, "call", {"service": service, "method": method, "args": args})

# log in the given database
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
uid = call(url, "common", "login", DB, USER, PASS)

# create a new note
# args = {
#     'color': 8,
#     'memo': 'This is note from json rpc odoo',
#     'create_uid': uid,
# }
# create_note_id = call(url, "object", "execute", DB, uid, PASS, 'note.note', 'create', args)
# print(create_note_id)

args = {
    'name': "El-Mohammady",
    'age': 24,
    'create_uid': uid,
}
create_patient_id = call(url, "object", "execute", DB, uid, PASS, 'hospital.patient', 'create', args)
print("create_patient_id",create_patient_id)


# Read record using json_rpc
# read_record = call(url, "object", "execute", DB, uid, PASS, 'hospital.patient', 'read', [2,16])
read_record = call(url, "object", "execute", DB, uid, PASS, 'hospital.patient', 'read', [create_patient_id])
print("read_record",read_record[0]["name"])
print("read_record",read_record[0])
# print("read_record",read_record[1])


# write/update record (write method)
vals = {
    'name': "3li El-Mohammady",
    'age': 24,
    'create_uid': uid,
}
update_patient_id = call(url, "object", "execute", DB, uid, PASS, 'hospital.patient', 'write',[create_patient_id], vals)
print("Update_patient_id",update_patient_id)



# delete record (unlink method)
delete_patient_id = call(url, "object", "execute", DB, uid, PASS, 'hospital.patient', 'unlink',[create_patient_id])
print("delete_patient_id",delete_patient_id)










