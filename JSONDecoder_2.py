# Creating a custom JSONDecoder using the point schema.

import json
import re
from pprint import pprint
from decimal import Decimal

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

class CustomDecoder(json.JSONDecoder):
    base_decoder = json.JSONDecoder(parse_float = Decimal)
    def decode(self, arg):
        obj = self.base_decoder.decode(arg)
        pattern = r'"_type"\s*:\s*"point"'
        if re.search(pattern, arg):
            obj = self.make_pts(obj)
        return obj

    def make_pts(self, obj):
        if isinstance(obj, dict):
            if obj.get('_type', None) == 'point':
                obj = Point(obj['x'], obj['y'])
            else:
                for key, value in obj.items():
                    obj[key] = self.make_pts(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.make_pts(item)
        return obj

j = '''
{
    "a": 100,
    "b": 0.5,
    "rectangle": {
        "corners": {
            "b_left": {"_type": "point", "x": -1, "y": -1},
            "b_right": {"_type": "point", "x": 1, "y": -1},
            "t_left": {"_type": "point", "x": -1, "y": 1},
            "t_right": {"_type": "point", "x": 1, "y": 1}
            },
        "rotate": {"_type": "point", "x": 0, "y": 0},
        "interior_pts": [
            {"_type": "point", "x":0, "y":0},
            {"_type": "point", "x":0.5, "y":0.5}
            ]
        }
    }
'''

pprint(json.loads(j, cls=CustomDecoder))
