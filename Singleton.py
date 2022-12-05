# Simple Singleton object

class Hundred:
    _existing_instance = None

    def __new__(cls):
        if not cls._existing_instance:
            print('Creating new instance...')
            new_instance = super().__new__(cls)
            setattr(new_instance, 'name', 'hundred')
            setattr(new_instance, 'value', 100)
            cls._existing_instance = new_instance
        else:
            print('Instance exists already, using that one...')
        return cls._existing_instance

h1 = Hundred()
h2 = Hundred()
h3 = Hundred()
print(h1 is h2)
print(h2 is h3)
