from collections import UserDict
from numbers import Real

class IntDict(UserDict):
    def __setitem__(self, key, value):
        if not isinstance(value, Real):
            raise ValueError('Value must be a Real Number')
        super().__setitem__(key, value)
    def __getitem__(self, key):
        return int(super().__getitem__(key))

class LimitedDict(UserDict):
    def __init__(self, keyset, min_value, max_value, *args, **kwargs):
        self._keyset = keyset
        self._min_value = min_value
        self._max_value = max_value
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if key not in self._keyset:
            raise KeyError('Invalid KeyName')
        if not isinstance(value, int):
            raise ValueError('Value must be an Integer type')
        if value< self._min_value or value>self._max_value:
            raise ValueError(f'Value must be between {self._min_value} and {self._max_value}')
        super().__setitem__(key, value)
