# Serializing the objects which are not JSON serializable, using custom json formatter.
import json
from datetime import datetime
from decimal import Decimal

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
    
p = Person('John', 24)
pt1 = Point(10,20)
pt2 = Point(Decimal('10.5'), Decimal('100.2'))

log_record = {
    'time1' : datetime.utcnow(),
    'time2' : datetime.utcnow(),
    'message' : 'Testing...',
    'args' : {1,2,3},
    'Person': p,
    'Point_1': pt1,
    'Point_2': pt2
    }

def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
    else:
        try:
            return arg.toJSON()
        except AttributeError:
            try:
                return vars(arg)
            except TypeError:
                return str(arg)
            
print(json.dumps(log_record, default = custom_json_formatter))
