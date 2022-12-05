# Singleton object

class Singleton(type):
    instances = {}
    def __call__(cls, *args, **kwargs):
        print(f'Request received to create an instance of class: {cls}...')
        existing_instance = Singleton.instances.get(cls, None)
        if existing_instance is None:
            print('Creating instance for the first time...')
            Singleton.instances[cls] = super.__call__(*args, **kwargs)
        else:
            print('Using existing instance')
        return Singleton.instances[cls]
class Hundred(metaclass = Singleton):
    value = 100

class Thousand(metaclass = Singleton):
    value = 1000
class HundredFold(Hundred):
    value = 100*100

h1 = Hundred()
h2 = Hundred()
print(h1 is h2)
t1 = Thousand()
t2 = Thousand()
print(t1 is t2)
hf1 = HundredFold()
hf2 = HundredFold()
print(hf1 is hf2)
