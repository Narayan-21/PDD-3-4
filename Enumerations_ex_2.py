from enum import Enum
from functools import total_ordering

@total_ordering
class OrderedEnum(Enum):
    """ Create an ordering based on the member values.
        So member values have to support rich comparisons."""
    def __lt__(self, other):
        if isinstance(other, OrderedEnum):
            return self.value < other.value
        return NotImplemented

class Number(OrderedEnum):
    ONE = 1
    TWO = 2
    THREE = 3

class Dimension(OrderedEnum):
    D1 = 1,
    D2 = 1,1
    D3 = 1,1,1

print(Number.ONE < Number.TWO)
print(Dimension.D2 > Dimension.D3)
print(Number.ONE >= Number.ONE)
