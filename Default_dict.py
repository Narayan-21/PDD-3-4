from collections import defaultdict, namedtuple
from datetime import datetime
from functools import wraps

def function_stats():
    d = defaultdict(lambda: {'counts': 0, 'first_called': datetime.utcnow()})
    Stats = namedtuple('Stats', 'decorator data')
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            d[fn.__name__]['counts'] += 1
            return fn(*args, **kwargs)
        return wrapper
    return Stats(decorator, d)

stats = function_stats()

@stats.decorator
def func1():
    pass

@stats.decorator
def func2(x,y):
    pass

func1()
print(stats.data)
func2(10,20)
print(stats.data)
func1()
func2(10,10)
print(stats.data)
