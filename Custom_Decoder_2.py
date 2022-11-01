import json
from datetime import datetime

class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn
    def __repr__(self):
        return f'Person(name={self.name}, ssn={self.ssn})'

j='''{
    "accountHolder": {
        "objecttype": "person",
        "name": "Eric Idel",
        "ssn": 100
        },
    "created": {
            "objecttype": "datetime",
            "value" : "2020-11-11T02:09:10"
            }
        }'''

def custom_decoder(arg):
    ret_val = arg
    if 'objecttype' in arg:
        if arg['objecttype'] == 'datetime':
            ret_val = datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
        elif arg['objecttype'] == 'fraction':
            ret_val = Fraction(arg['numerator'],arg['denominator'])
        elif arg['objecttype'] == 'person':
            ret_val = Person(arg['name'],arg['ssn'])
    return ret_val

print(json.loads(j, object_hook=custom_decoder))
