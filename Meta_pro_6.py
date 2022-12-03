# Here, the standalone say_hello() function in the Person class is transformed into the instance
# of the class Logger. To transform it back to the method when being called from the instance, hence
# we need to implement the descriptor protocol, so we define __get__ method in the Logger class.


from types import MethodType

class Logger:
    def __init__(self, fn):
        self.fn = fn
    def __call__(self, *args, **kwargs):
        print(f'Log: {self.fn.__name__} called..')
        return self.fn(*args, **kwargs)
    def __get__(self, instance, owner_class):
        print(f'__get__called: self={self}, instance={instance}')
        if instance is None:
            print('\treturning self unbound...')
            return self
        else:
            print('\treturning self as a method bound to instance')
            return MethodType(self, instance)

class Person:
    def __init__(self, name):
        self.name = name
    @Logger
    def say_hello(self):
        return f'{self.name} says hello'
    @classmethod
    @Logger
    def cls_method(cls):
        print('Class method called...')
    @staticmethod
    @Logger
    def static_method():
        print('Static method called...')
    
p = Person('Alex')
p.say_hello()
p.cls_method()
p.static_method()
