from pprint import pprint

class SlottedStruct(type):
    def __new__(mcls, name, bases, class_dict):
        cls_object = super().__new__(mcls, name, bases, class_dict)

        # __slots__
        setattr(cls_object, '__slots__', [f'_{field}'for field in cls_object._fields])

        # read-only properties
        for field in cls_object._fields:
            slot = f'_{field}'
            setattr(cls_object, field, property(fget=lambda self, attrib=slot: getattr(self, attrib)))

        # __eq__
        def eq(self, other):
            if isinstance(other, cls_object):
                self_fields = [getattr(self, field) for field in cls_object._fields]
                other_fields = [getattr(other, field) for field in cls_object._fields]
                return self_fields == other_fields
            return False
        setattr(cls_object, '__eq__', eq)

        # __hash__
        def hash_(self):
            field_values = (getattr(self, field) for field in cls_object._fields)
            return hash(tuple(field_values))            
        setattr(cls_object, '__hash__', hash_)

        # __str__
        def str_(self):
            field_values = (getattr(self, field) for field in cls_object._fields)
            field_values_joined = ', '.join(map(str, field_values))
            return f'{cls_object.__name__}({field_values_joined})'
        setattr(cls_object, '__str__', str_)

        # __repr__
        def repr_(self):
            field_values = (getattr(self, field) for field in cls_object._fields)
            field_key_values = (f'{key} = {value}'for key, value in zip(cls_object._fields, field_values))
            field_key_values_str = ', '.join(field_key_values)
            return f'{cls_object.__name__}({field_key_values_str})'
        setattr(cls_object, '__repr__', repr_)
        
        return cls_object

def struct(cls):
    return SlottedStruct(cls.__name__, cls.__bases__, dict(cls.__dict__))

class Point2D(metaclass=SlottedStruct):
    _fields = ['x', 'y']
    def __init__(self, x, y):
        self._x = x
        self._y = y
        
# Or use the struct decorator
@struct
class Point3D:
    _fields = ['x', 'y', 'z']
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

p1 = Point3D(1,2,1)
p2 = Point3D(1,2,1)
p3 = Point3D(0,0,2)
