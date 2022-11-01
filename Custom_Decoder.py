# Creating a custom decoder using Schema to deserialize the datetime string.

import json
from datetime import datetime
from fractions import Fraction

j='''{
"time": {
    "objecttype": "datetime",
    "value": "2018-10-21T09:14:15"
    },
"frac": {
    "objecttype": "fraction",
    "numerator": 20,
    "denominator": 25
    },
"message": "Created this json string"
}
'''

def custom_decoder(arg):
    ret_val = arg
    if 'objecttype' in arg:
        if arg['objecttype'] == 'datetime':
            ret_val = datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
        elif arg['objecttype'] == 'fraction':
            ret_val = Fraction(arg['numerator'],arg['denominator'])
    return ret_val


print(json.loads(j, object_hook=custom_decoder))
