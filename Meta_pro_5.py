import inspect
from functools import wraps

def func_logger(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f'Log: {fn.__qualname__}({args}, {kwargs}) = {result}')
        return result
    return inner

def class_logger(cls):
    for name, obj in vars(cls).items():
        if isinstance(obj, staticmethod):
            type_ = type(obj)
            original_func = obj.__func__
            decorated_func = func_logger(original_func)
            method = type_(decorated_func)
            setattr(cls, name, method)
            
        elif isinstance(obj, property):
            print('Decorating property', cls, name)
            methods = (('fget','getter'), ('fset','setter'),('fdel','deleter'))
            for prop, method  in methods:
                if getattr(obj, prop):
                    obj = getattr(obj, method)(func_logger(getattr(obj, prop)))
            setattr(cls, name, obj)
            
        elif inspect.isroutine(obj):
            print('Decorating callable', cls, name)
            original_func = obj
            decorated_func = func_logger(original_func)
            setattr(cls, name, decorated_func)
    return cls

@class_logger
class MyClass:
    @staticmethod
    def static_method():
        pass
    @classmethod
    def cls_method():
        pass
    def inst_method(self):
        pass
    @property
    def name(self):
        pass
    def __add__(self, other):
        pass
    @class_logger
    class Other:
        def __call__(self):
            pass
    other = Other()
    
keys = ('static_method', 'cls_method', 'inst_method', 'name', '__add__', 'Other', 'other')
inspect_funcs = ('isroutine', 'ismethod', 'isfunction', 'isbuiltin', 'ismethoddescriptor')

max_header_length = max(len(key) for key in keys)
max_fname_length = max(len(func) for func in inspect_funcs)
print(format('',f'{max_fname_length}s'),'\t'.join(format(key,f'{max_header_length}s') for key in keys))
for inspect_func in inspect_funcs:
    fn = getattr(inspect, inspect_func)
    inspect_results = (format(str(fn(MyClass.__dict__[key])), f'{max_header_length}s') for key in keys)
    print(format(inspect_func, f'{max_fname_length}s'),'\t'.join(inspect_results))
