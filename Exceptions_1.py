import json

json_data = """{
"Alex" : {"age": 18},
"Bryan" : {"age": 21, "city": "London"},
"Guido" : {"age": "unknown"}
}"""

data = json.loads(json_data)

class Person:
    __slots__ = 'name', '_age'
    def __init__(self, name):
        self.name = name
        self._age = None
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError('Invalid Age')
    def __repr__(self):
        return f'Person((name={self.name}, age={self.age}))'

persons = []

for name, attributes in data.items():
    try:
        p = Person(name)
        for attrib_name, attrib_value in attributes.items():
            try:
                setattr(p, attrib_name, attrib_value)
            except AttributeError:
                print(f'ignoring attribute: {name}.{attrib_name}={attrib_value}')
    except ValueError as ex:
        print(f'Data for Person({name}) contains an invalid attribute value: {ex}')
    else:
        persons.append(p)

print(persons) 
