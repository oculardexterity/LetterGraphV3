
import xmlrpc.client

# Farm this out somewhere decent
STATUS = 'development'



# Don't do this hacky shit
import sys, os
sys.path.append('../LetterGraphV3')

from config import exist_config







rpc_string = 'http://{user_name}:{password}@{address}:{port}/exist/xmlrpc'
rpc_address = rpc_string.format_map(exist_config[STATUS])

rpc = xmlrpc.client.ServerProxy(rpc_address, encoding='UTF-8', verbose=False)
print(rpc)


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

