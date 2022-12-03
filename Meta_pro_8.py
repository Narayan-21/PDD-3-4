class AutoClassAttirb(type):
    def __new__(mcls, name, bases, cls_dict, **extra_attrs):
        print('Creating class with some extra attributes:', extra_attrs)
        new_cls = super().__new__(mcls, name, bases, cls_dict)
        if extra_attrs:
            for attr_name, attr_value in extra_attrs.items():
                setattr(new_cls, attr_name, attr_value)
        return new_cls

class Account(metaclass=AutoClassAttirb, account_type='Savings', apr=0.2):
    pass

print(Account.__dict__)
