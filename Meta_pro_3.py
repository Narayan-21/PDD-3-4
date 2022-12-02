from functools import wraps
from pprint import pprint

def func_logger(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f'Log: {fn.__qualname__}({args}, {kwargs}) = {result}')
        return result
    return inner

def class_logger(cls):
    for name, obj in vars(cls).items():
        if callable(obj):
            print('decorating:', cls, name)
            setattr(cls, name, func_logger(obj))
    return cls

@class_logger
class Person:
    @staticmethod
    def static_method():
        print('Static_method invoked...')
    @classmethod
    def cls_method(cls):
        print(f'cls_method invoked for {cls}....')
    def instance_method(self):
        print(f'instance_method invoked for {self}...')

pprint(Person.__dict__)
