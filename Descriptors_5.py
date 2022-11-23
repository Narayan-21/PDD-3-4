class ValidString:
    def __init__(self, min_length=None):
        self.min_length = min_length
    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a string.')
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(
                f'{self.property_name} must be at least {self.min_length} characters.'
                )
        instance.__dict__[self.property_name] = value
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        print('__get__ method called...')
        return instance.__dict__.get(self.property_name, None)

class Person:
    first_name = ValidString(1)
    last_name = ValidString(2)
    
p = Person()

p.first_name = 'Alex'
print(p.__dict__)
print(p.first_name)
