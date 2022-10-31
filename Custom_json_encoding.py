# Serializing the objects which are not JSON serializable, using custom json formatter.
import json
from datetime import datetime

log_record = {
    'time1' : datetime.utcnow(),
    'time2' : datetime.utcnow(),
    'message' : 'Testing...',
    'args' : {1,2,3}
    }

def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)

print(json.dumps(log_record, default = custom_json_formatter))
