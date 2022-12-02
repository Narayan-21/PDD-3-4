# Here, first we will unwrap the static and class method, then decorate the original function then re-wrap them with those decorators back.

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
            print('Decorating callable', cls, name)
            original_func = obj
            decorated_func = func_logger(original_func)
            setattr(cls, name, decorated_func)
        elif isinstance(obj, staticmethod):
            print('Decorating static method', cls, name)
            original_func = obj.__func__
            decorated_func = func_logger(original_func)
            method = staticmethod(decorated_func)
            setattr(cls, name, method)
        elif isinstance(obj, classmethod):
            print('Decorating class method', cls, name)
            original_func = obj.__func__
            decorated_func = func_logger(original_func)
            method = classmethod(decorated_func)
            setattr(cls, name, method)
        elif isinstance(obj, property):
            print('Decorating property', cls, name)
            if obj.fget:
                obj = obj.getter(func_logger(obj.fget))
            if obj.fset:
                obj = obj.setter(func_logger(obj.fset))
            if obj.fdel:
                obj = obj.deleter(func_logger(obj.fdel))
            setattr(cls, name, obj)
    return cls

@class_logger
class Person:
    def __init__(self, name):
        self._name = name
    @staticmethod
    def staticmethod(a,b):
        print('static_method called....', a,b)
    @classmethod
    def class_method(cls, a, b):
        print('class_method called....',a,b)
    def instance_method(self, a, b):
        print('instance_method called...',a,b)
    @property
    def name(self):
        return self._name

p = Person('David')
print(p)
