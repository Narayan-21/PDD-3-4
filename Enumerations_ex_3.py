import enum
import random
from pprint import pprint

random.seed(0)

class State_1(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        while True:
            new_value = random.randint(1,100)
            if new_value not in last_values:
                return new_value
            
    a = enum.auto()
    b = enum.auto()
    c = enum.auto()
    d = enum.auto()

for member in State_1:
    print(member.name, member.value)

class State_2(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.title()
    WAITING = enum.auto()
    STARTED = enum.auto()
    FINISHED = enum.auto()

for member in State_2:
    print(member.name, member.value)

class Aliased_1(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        print(f'count={count}')
        if count % 2 ==1:
            # make this member an alias of the previous one.
            return last_values[-1]
        else:
            return last_values[-1] + 1
    GREEN = 1
    GREEN_ALIAS = 2
    RED = 10
    CRIMSON = enum.auto()
    BLUE = enum.auto()
    AQUA =  enum.auto()

class Aliased_2(enum.Enum):
    def _generate_next_value_(name, start, count, last_values):
        return last_values[-1]
class Color(Aliased_2):
    RED = object()
    CRIMSON = enum.auto()
    CARMINE = enum.auto()
    BLUE = object()
    AQUAMARINE = enum.auto()
    AZURE = enum.auto()

pprint(Color.__members__)
print(list(Color))
