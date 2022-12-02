import math

class CustomType(type):
    def __new__(cls, name, base, class_dict):
        print('Customized type creation!')
        cls_obj = super().__new__(cls, name, base, class_dict)
        cls_obj.circ = lambda self: 2*self.pi*self.r
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

Circle = CustomType('Circle', (), class_dict)
print(Circle)
type(Circle)
print(isinstance(Circle, type))

c = Circle(0,0,1)
print(c.area())
