# Creating a custom memoizer, in which the argument positions do not matter while calling the function.
# Created using dictionary and frozenset.

def memoizer(fn):
    cache={}
    def inner(*args, **kwargs):
        key = (*args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        else:
            result = fn(*args, **kwargs)
            cache[key] = result
            return result
    return inner

@memoizer
def func(*,a,b):
    print('Calculating a+b..')
    return a+b

print(func(a=1,b=3))
print(func(a=1,b=3))
print(func(b=3,a=1))
