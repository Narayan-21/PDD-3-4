# Validating one dictionary structure against template dictionary.

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
        return False, ' '.join((missing_msg,',', extras_msg))
    else:
        return True, None

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
            return False, err_msg
    return True, None

def recurse_validate(data, template, path):
    is_ok, err_msg = match_keys(data, template, path)
    if not is_ok:
        return False, err_msg

    is_ok, err_msg = match_types(data, template, path)
    if not is_ok:
        return False, err_msg

    dictionary_type_keys = {key for key,value in template.items()
                            if isinstance(value, dict)}
    for key in dictionary_type_keys:
        sub_path = path + '.'+ str(key)
        sub_template = template[key]
        sub_data = data[key]
        is_ok, err_msg = recurse_validate(sub_data, sub_template, sub_path)
        if not is_ok:
            return False, err_msg
        
    return True, None

def validate(data, template):
    return recurse_validate(data, template, '')

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
for person, name in persons:
    is_ok, err_msg = validate(person, template)
    print(f'{name}: valid={is_ok}: {err_msg}')
    
