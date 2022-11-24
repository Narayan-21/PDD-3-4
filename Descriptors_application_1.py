import numbers

class ValidType:
    def __init__(self, type_):
        self._type = type_
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise ValueError(f'{self.prop_name} must be of type {self._type.__name__}.')
        instance.__dict__[self.prop_name] = value
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)

class Person:
    age = ValidType(int)
    height = ValidType(numbers.Real)
    tags = ValidType(list)
    favorite_foods = ValidType(tuple)

p = Person()
try:
    p.height = 10
except ValueError as ex:
    print(ex)
