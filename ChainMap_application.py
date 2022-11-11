# Creating a custom config dictionary with a local config setting.

from collections import ChainMap

config = {
    'host': 'prod.deepdive.com',
    'port': 5432,
    'database': 'deepdive',
    'user_id': '$pg_user',
    'user_pwd': '$pg_pwd'
    }

local_config = ChainMap({}, config)
print(list(local_config.items()))

local_config['user_id'] = 'test'
local_config['user_pwd'] = 'test'

print(list(local_config.items()))
