# Serializing a custom class by creating toJSON() function in that class.

import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    def toJSON(self):
        return dict(name=self.name, age=self.age)

p = Person('John',22)
ser = json.dumps({'json': p.toJSON()}, indent=2)
print('Serialized Custom Class - ',ser)
deser = json.loads(ser)
print('Deserialized Custom Class - ', deser)
