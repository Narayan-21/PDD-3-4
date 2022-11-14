# Creating attributes at runtime

from types import MethodType

class Person:
    def __init__(self, name):
        self.name = name
    def register_do_work(self, func):
        setattr(self, '_do_work', MethodType(func, self))
    def do_work(self):
        do_work_method = getattr(self, '_do_work', None)
        if do_work_method:
            return do_work_method()
        else:
            raise AttributeError('You must first register a do_work method.')

def work_math(self):
    return f'{self.name} will teach differentials today.'

def work_english(self):
    return f'{self.name} will analyze Hamlet today.'

english_teacher = Person('Eric')
math_teacher = Person('John')

math_teacher.register_do_work(work_math)
english_teacher.register_do_work(work_english)

persons = [math_teacher, english_teacher]
for p in persons:
    print(p.do_work())
