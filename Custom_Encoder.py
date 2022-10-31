# Creating a custom encoder while skipping the keys that are not serializable.

import json
from datetime import datetime

class CustomEncoder1(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super().__init__(skipkeys=True,
                         allow_nan=False,
                         indent='---',
                         separators=('', ' = '))
    def default(self, arg):
        if isinstance(arg, datetime):
            return arg.isoformat()
        else:
            return super().default(arg)

d_1 = {
    'time': datetime.utcnow(),
    1+1j : "Complex",
    'name': 'Python'
    }

print(json.dumps(d_1, cls=CustomEncoder1))


class CustomEncoder2(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, datetime):
            obj = dict(
                datatype= "datetime",
                iso = arg.isoformat(),
                date = arg.date().isoformat(),
                time = arg.time().isoformat(),
                year = arg.year,
                month = arg.month,
                day = arg.day,
                hour = arg.hour,
                minutes = arg.minute,
                seconds = arg.second
                )
            return obj
        else:
            return super().default(arg)

d_2 = {'time': datetime.utcnow()}
print(json.dumps(d_2, cls=CustomEncoder2, indent=2))
