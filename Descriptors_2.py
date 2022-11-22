class IntegerValue:
    def __init__(self):
        self.values = {}
    def __set__(self, instance, value):
        self.values[instance] = int(value)
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return self.values.get(instance)

class Point2D:
    x = IntegerValue()
    y = IntegerValue()

p1 = Point2D()
p2 = Point2D()
p1.x = 10.1
p1.y = 20.2
p2.x = 100.1
p2.y = 200.2

print(Point2D.x.values)
print(Point2D.y.values)
