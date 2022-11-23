import ctypes
import weakref

def ref_count(address):
    return ctypes.c_long.from_address(address).value

class IntegerValue:
    def __init__(self):
        self.values = {}
    def __set__(self, instance, value):
        self.values[id(instance)] = (weakref.ref(instance, self._remove_object), int(value))
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values[id(instance)][1]
    def _remove_object(self, weak_ref):
        reverse_lookup = [key for key, value in self.values.items()
                          if value[0] is weak_ref]
        if reverse_lookup:
            key = reverse_lookup[0]
            del self.values[key]

class Point:
    x = IntegerValue()
