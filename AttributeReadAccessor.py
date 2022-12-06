# Example 1

class Person_1:
    def __getattr__(self, name):
        alt_name = '_'+name
        print(f'Could not find {name}, trying {alt_name}...')
        try:
            return super().__getattribute__(alt_name)
        except AttributeError:
            raise AttributeError(f'Could not find {name} or {alt_name}')

p_1 = Person_1()
try:
    p_1.age
except AttributeError as ex:
    print(type(ex).__name__, ex)

# Example 2

class Person_2:
    def __init__(self, age):
        self._age = age
    def __getattr__(self, name):
        alt_name = '_' + name
        print(f'Could not find {name}, trying {alt_name}...')
        try:
            return super().__getattribute__(alt_name)
        except AttributeError:
            raise AttributeError(f'Could not find {name} or {alt_name}')

p_2 = Person_2(22)
print(p_2.age)


# Example_3

class DefaultClass:
    def __init__(self, attribute_default=None):
        self._attribute_default = attribute_default
    def __getattr__(self, name):
        print(f'{name} not found, creating it and setting it to default...')
        setattr(self, name, self._attribute_default)
        return self._attribute_default

class Person_3(DefaultClass):
    def __init__(self, name):
        super().__init__('Unavailable')
        self.name = name

p3 = Person_3('Raymond')
print(p3.age)
