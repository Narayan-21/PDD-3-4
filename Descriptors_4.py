import weakref
from pprint import pprint

class ValidString:
    def __init__(self, min_length=0, max_length=255):
        self.data = {}
        self._min_length = min_length
        self._max_length = max_length
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('Value must be a string')
        if len(value)< self._min_length:
            raise ValueError(
                f'Value should be at least {self._min_length} characters.'
                )
        if len(value)>self._max_length:
            raise ValueError(
                f'Value cannnot exceed {self._max_length} characters.'
                )
        self.data[id(instance)] = (weakref.ref(instance, self._finalize_instance), value)
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            value_tuple = self.data.get(id(instance))
            return value_tuple[1]
    def _finalize_instance(self, weak_ref):
        for key, value in self.data.items():
            if value[0] is weak_ref:
                del self.data[key]
                break

class Person:
    __slots = '__weakref__'
    first_name = ValidString(1,100)
    last_name = ValidString(1,100)
    def __eq__(self, other):
        return (
            isinstance(other, Person) and
            self.first_name == other.first_name and
            self.last_name == other.last_name
            )

class BankAccount:
    __slots__ = '__weakref__'
    account_number = ValidString(5,255)
    def __eq__(self, other):
        return isinstance(other, BankAccount) and self.account_number == other.account_number
    
p1 = Person()
p2 = Person()
p1.first_name, p1.last_name = 'Guido', 'Van Russum'
p2.first_name, p2.last_name = 'Raymond', 'Hettinger'
b1, b2 = BankAccount(), BankAccount()
b1.account_number, b2.account_number = 'Savings', 'Checking'
print(p1.first_name, p1.last_name)
print(p2.first_name, p2.last_name)
print(b1.account_number, b2.account_number)
pprint(Person.first_name.data)
pprint(Person.last_name.data)
pprint(BankAccount.account_number.data)
del p1, p2, b1, b2
print(Person.first_name.data)
