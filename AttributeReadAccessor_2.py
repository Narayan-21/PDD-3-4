class DefaultClass:
    def __init__(self, attribute_default=None):
        self._attribute_default = attribute_default
    def __getattr__(self, name):
        print(f'{name} not found, creating it and setting it to default...')
        default_value = super().__getattribute__('_attribute_default')
        setattr(self, name, default_value)
        return default_value

class Person(DefaultClass):
    def __init__(self, name, age):
        super().__init__('Not Available')
        if name is not None:
            self._name = name
        if age is not None:
            self._age = age
    def __getattribute__(self, name):
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError(f'Forbidden access to {name}')
        return super().__getattribute__(name)
    @property
    def name(self):
        return super().__getattribute__('_name')
    @property
    def age(self):
        return super().__getattribute__('_age')

p = Person('Python',43)
print(p.name, p.age)
print(p.language)
print(p.__dict__)
    
