from json import load, loads, JSONDecodeError
from jsonschema import validate
from jsonschema.exceptions import ValidationError

person_schema = {
    "type": "object",
    "properties" : {
        "firstname": {
            "type": "string",
            "minLength": 1
            },
        "middleInitial": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1
            },
        "lastName": {
            "type": "string",
            "minLength": 1
            },
        "age": {
            "type": "integer",
            "minimun": 0
            },
        "eyeColor": {
            "type": "string",
            "enum": ["amber", "blue", "brown", "gray", "green", "hazel", "red", "violet"]
            }
        },
    "required": ["firstName", "lastName"]
}

p1 = '''
{
    "firstName": "John",
    "middleInitial": "M",
    "lastName": "Cleese",
    "age": 33
}'''

p2 = '''
{
    "firstName": "John",
    "middleInitial": 100,
    "lastName": "Cleese",
    "age": "Unknown"
}'''

p3 = '''
{
    "firstName": "John",
    "age": -10.4
}'''

person = p1

try:
    validate(loads(person), person_schema)
except JSONDecodeError as ex:
    print(f'Invalid JSON: {ex}')
except ValidationError as ex:
    print(f'Validation error: {ex}')
else:
    print('JSON is Valid and confirms to schema')
