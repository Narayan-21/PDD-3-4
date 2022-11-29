class ConversionError(Exception):
    pass

def make_bool(val):
    if isinstance(val, int):
        if val in {0,1}:
            return bool(val)
        else:
            raise ConversionError('Invalid Integer value')
    if isinstance(val, str):
        if val.casefold() in {'1','true','t'}:
            return True
        if val.casefold() in {'0','false','f'}:
            return False
        raise ConversionError('Invalid String value')
    raise ConversionError('Invalid Type')

values = [True, 0, 'T', 'false', 10, 'ABC', 1.0]

for value in values:
    try:
        result = make_bool(value)
    except ConversionError as ex:
        result = str(ex)
    print(value, result)

