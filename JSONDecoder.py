import json

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'
    
class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        obj = json.loads(arg)
        if 'points' in obj:
            obj['points'] = [Point(x,y) for x, y in obj['points']]
        return obj

j_points = '''
{
    "points": [
        [10,20],
        [-1,-2],
        [0.5,0.3]
        ]
    }
'''

print(json.loads(j_points, cls = CustomDecoder))
