import mimetypes
import os
import xmlrpc.client

# Farm this out somewhere decent
STATUS = 'development'



# Don't do this hacky shit
import sys, os
sys.path.append('../LetterGraphV3')

from config import EXIST_CONFIG







rpc_string = 'http://{username}:{password}@{address}:{port}/exist/xmlrpc'
rpc_address = rpc_string.format_map(EXIST_CONFIG[STATUS])

rpc = xmlrpc.client.ServerProxy(rpc_address, encoding='UTF-8', verbose=False)


xqpath = 'LetterGraph/Server/xqueries'
file = sorted(os.listdir(xqpath))[1]

file_path = os.path.join(xqpath, file)



with open(file_path, 'rb') as f:
    to_up = f.read()



f_id = rpc.upload(to_up, len(to_up))
rpc.parseLocal(f_id, '/db/apps/testapp/new_test_file.xql', 1, 'application/xquery')





"""

query = '''

xquery version "3.1";

let $thing := "boffin"
return <test>{$thing}</test>

'''
vars = {'x': 'testy'}

res = rpc.execute('/db/apps/testapp/test.xql', {'variables': vars})
print('RES_ID: ', res)





res = rpc.retrieve(res['id'], 0, {})
print(res)

#params = ({'indent': 'yes'})

#xml_query = xmlrpc.client.dumps(params, methodname='query')

#print(xml_query)

#meths = rpc.system.listMethods()
#print(meths)

"""