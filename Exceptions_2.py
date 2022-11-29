def convert_int(val):
    if not isinstance(val, int):
        raise TypeError()
    if val not in {0,1}:
        raise ValueError('Integer values 0 or 1 only')
    return bool(val)

def convert_str(val):
    if not isinstance(val, str):
        raise TypeError()
    val = val.casefold()
    if val in {'0','f','false'}:
        return False
    elif val in {'1','t','true'}:
        return True
    else:
        raise ValueError('Admissible string values are: T, F, True, False, 0, 1 etc..')

class ConversionError(Exception):
    pass

def make_bool(val):
    try:
        try:
            b = convert_int(val)
        except TypeError:
            try:
                b = convert_str(val)
            except TypeError:
                raise ConversionError(f'The type is inadmissible...')
    except ValueError as ex:
        raise ConversionError(f'The value {val} cannot be converted to a bool: {ex}')
    else:
        return b

values = [True, 0, 'T', 'false', 10, 'ABC', 1.0]

for value in values:
    try:
        result = make_bool(value)
    except ConversionError as ex:
        result = str(ex)
    print(value, result)

    
