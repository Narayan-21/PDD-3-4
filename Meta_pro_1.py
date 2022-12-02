import math

class CustomType(type):
    def __new__(cls, name, base, class_dict):
        print('Customized type creation!')
        cls_obj = super().__new__(cls, name, base, class_dict)
        cls_obj.circ = lambda self: 2*math.pi*self.r
        return cls_obj

class_body = """
def __init__(self, x,y,r):
	self.x = x
	self.y= y
	self.r = r
def area(self):
	return math.pi*self.r**2
"""
class_dict = {}

exec(class_body, globals(), class_dict)

Circle_1 = CustomType('Circle', (), class_dict)
print(Circle_1)
type(Circle_1)
print(isinstance(Circle_1, type))

c_1 = Circle_1(0,0,1)
print(c_1.area())

class Circle_2(metaclass=CustomType):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    def area(self):
        return math.pi* self.r**2

c_2 = Circle_2(0,0,2)
print(c_2.area())
print(c_2.circ())
