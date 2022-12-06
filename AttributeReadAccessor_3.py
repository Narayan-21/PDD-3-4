class MetaLogger(type):
    def __getattribute__(self, name):
        print('Class __getattribute__ called...')
        return super().__getattribute__(name)
    def __getattr__(self, name):
        print('Class __getattr__ called...')
        return 'Not Found'

class Account(metaclass = MetaLogger):
    apr = 10

print(Account.apr)    
print(Account.apy)  
