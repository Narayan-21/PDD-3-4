from functools import wraps

def func_logger(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f'Log: {fn.__qualname__}({args},{kwargs}) = {result}')
        return result
    return inner

class Person:
    @func_logger
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @func_logger
    def greet(self):
        return f'Hello, my name is {self.name}, and I am {self.age} years old.'

p = Person('John', 22)
print(p)
print(p.greet())
