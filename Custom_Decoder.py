# Creating a custom decoder using Schema to deserialize the datetime string.

import json
from datetime import datetime

j='''{
"time": {
    "objecttype": "datetime",
    "value": "2018-10-21T09:14:15"
    },
    "message": "Created this json string"
}
'''

def custom_decoder(arg):
    if 'objecttype' in arg and arg['objecttype'] == 'datetime':
        return datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
    else:
        return arg

print(json.loads(j, object_hook=custom_decoder))
