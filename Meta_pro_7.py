from functools import wraps

def func_logger(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f'Log: {fn.__qualname__}({args},{kwargs}) = {result}')
        return result
    return inner


class ClassLogger(type):
    def __new__(mcls, name, bases, class_dict):
        cls = super().__new__(mcls, name, bases, class_dict)
        for name, obj in cls.__dict__.items():
            if callable(obj):
                print('decorating:', cls, name)
                setattr(cls, name, func_logger(obj))
        return cls

class Person(metaclass=ClassLogger):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f'Hello, my name is {self.name} and I am {self.age} years old.'
    
class Student(Person):
    def __init__(self, name, age, student_number):
        super().__init__(name, age)
        self.student_number = student_number
    def study(self):
        return f'{self.name} studies...'

p = Person('Alex',22)
#p.greet()
s = Student('Alex', 21, 'abc')

