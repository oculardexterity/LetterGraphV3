import xmlrpc.client

# Farm this out somewhere decent
STATUS = 'development'


# Don't do this hacky shit
import sys, os
sys.path.append('../LetterGraphV3')

from config import exist_config



rpc_string = 'http://{user_name}:{password}@{address}:{port}/exist/xmlrpc'
rpc_address = rpc_string.format_map(exist_config[STATUS])

rpc = xmlrpc.client.ServerProxy(rpc_address)
print(rpc)

rpc.removeCollection('/db/apps/TEST_COLL')

