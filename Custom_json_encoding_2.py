# Serializing the objects which are not JSON serializable, using singledispatch decorator

import json
from decimal import Decimal
from fractions import Fraction
from functools import singledispatch
from datetime import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.utcnow()
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    def toJSON(self):
        return vars(self)
    
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'
    
@singledispatch
def json_format(arg):
    print(arg)
    try:
        print('\ttrying to use toJSON()...')
        return arg.toJSON()
    except AttributeError:
        print('\tFailed - trying to use vars...')
        try:
            return vars(arg)
        except TypeError:
            print('\tFailed - using string repr...')
            return str(arg)

@json_format.register(datetime)
def _(arg):
    return arg.isoformat()

@json_format.register(set)
def _(arg):
    return list(arg)
@json_format.register(Decimal)
def _(arg):
    return f'Decimal({str(arg)})'

d= dict(a=1+1j,
        b=Decimal('0.5'),
        c= Fraction(1,3),
        p = Person('python', 23),
        pt = Point(0,0),
        time = datetime.utcnow()
        )
print(json.dumps(d, default=json_format))
