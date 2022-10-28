# Validating one dictionary structure against template dictionary.

class SchemaError(Exception):
    pass

class SchemaKeyMismatch(SchemaError):
    pass

class SchemaTypeMismatch(SchemaError, TypeError):
    pass

def match_keys(data, valid, path):
    data_keys = data.keys()
    valid_keys = valid.keys()

    extra_keys = data_keys - valid_keys
    missing_keys = valid_keys - data_keys

    if missing_keys or extra_keys:
        missing_msg = ('missing keys: '+
                       ', '.join({path+'.'+str(key) for key in missing_keys})
                       ) if missing_keys else ''
        extras_msg = ('extra keys: ' +
                      ', '.join({path + '.' + str(key) for key in extra_keys})
                      ) if extra_keys else ''
        raise SchemaKeyMismatch(' '.join((missing_msg,',', extras_msg)))

def match_types(data, template, path):
    for key, value in template.items():
        if isinstance(value, dict):
            template_type = dict
        else:
            template_type = value
        data_value = data.get(key, object())
        if not isinstance(data_value, template_type):
            err_msg = ('incorrect type: ' + path + '.' + key +
                       ' -> expected ' + template_type.__name__+
                       ', found ' + type(data_value).__name__)
            raise SchemaTypeMismatch(err_msg)

def recurse_validate(data, template, path):
    match_keys(data, template, path)
    match_types(data, template, path)
    dictionary_type_keys = {key for key,value in template.items()
                            if isinstance(value, dict)}
    for key in dictionary_type_keys:
        sub_path = path + '.'+ str(key)
        sub_template = template[key]
        sub_data = data[key]
        recurse_validate(sub_data, sub_template, sub_path)

def validate(data, template):
    recurse_validate(data, template, '')
    
template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
    },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
        },
        'birthplace': {
            'country': str,
            'city': str
        }
    }
}

john = {
    'user_id': 100,
    'name': {
        'first': 'John',
        'last': 'Cleese'
    },
    'bio': {
        'dob': {
            'year': 1939,
            'month': 11,
            'day': 27
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Weston-super-Mare'
        }
    }
}

eric = {
    'user_id': 101,
    'name': {
        'first': 'Eric',
        'last': 'Idle'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 3,
            'day': 29
        },
        'birthplace': {
            'country': 'United Kingdom'
        }
    }
}

michael = {
    'user_id': 102,
    'name': {
        'first': 'Michael',
        'last': 'Palin'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 'May',
            'day': 5
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Sheffield'
        }
    }
}

persons = ((john, 'John'),(eric, 'Eric'), (michael, 'Michael'))
#print(validate(john,template))
#print(validate(eric, template))
#print(validate(michael, template))


try:
        validate(michael, template)
except SchemaKeyMismatch as ex:
    print('Handling a key mismatch exception', ex)
except SchemaTypeMismatch as ex:
    print('Handling a type mismatch exception', ex)
except SchemaError as ex:
    print('Handling some general schema exception', ex)
except TypeError as ex:
    print('Handling a general type exception', ex)
