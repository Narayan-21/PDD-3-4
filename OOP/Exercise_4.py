from time import perf_counter, sleep
from functools import wraps
import random


def profiler(fn):
    _counter = 0
    _total_elapsed = 0
    _avg_time = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal _counter
        nonlocal _total_elapsed
        nonlocal _avg_time
        _counter += 1
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        _total_elapsed += (end-start)
        _avg_time = _total_elapsed / _counter
        return result
    def counter():
        return _counter
    def avg_time():
        return _avg_time
    inner.counter = counter
    inner.avg_time = avg_time
    return inner

@profiler
def func_1():
    sleep(random.random())

print(func_1(), func_1())
print(func_1.counter())
print(func_1.avg_time())

class Profiler_2:
    def __init__(self, fn):
        self.counter = 0
        self.total_elapsed = 0
        self.fn = fn
    def __call__(self, *args, **kwargs):
        self.counter += 1
        start = perf_counter()
        result = self.fn(*args, **kwargs)
        end = perf_counter()
        self.total_elapsed += (end - start)
        return result
    @property
    def avg_time(self):
        return self.total_elapsed / self.counter

@Profiler_2
def func_2(a,b):
    sleep(random.random())
    return (a,b)

print(func_2(1,3))
print(func_2.counter)
