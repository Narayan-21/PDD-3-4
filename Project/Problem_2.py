from datetime import date, datetime
import json
from decimal import Decimal

class Stock:
    def __init__(self, symbol, date, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def as_dict(self):
        return dict(symbol=self.symbol,
                    date = self.date,
                    open_ = self.open,
                    high = self.high,
                    low = self.low,
                    close = self.close,
                    volume = self.volume
                    )
    def __eq__(self, other):
        return isinstance(other, Stock) and self.as_dict() == other.as_dict()

class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol,
        self.timestamp = timestamp,
        self.order = order,
        self.price = price,
        self.commission = commission,
        self.volume = volume
        
    def as_dict(self):
        return dict(symbol = self.symbol,
                    timestamp = self.timestamp,
                    order = self.order,
                    price = self.price,
                    commission = self.commission,
                    volume = self.volume
                    )
    def __eq__(self, other):
        return isinstance(other, Trade) and self.as_dict() == other.as_dict()
    
activity = {
    "quotes": [
        Stock('TSLA', date(2018,11,22),
              Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.64'), 365_607),
        Stock('AAPL', date(2018,11,22),
              Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), 3_699_184),
        Stock('MSFT', date(2018, 11, 22),
              Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'), 4_493_689)
        ],
    "trades": [
        Trade('TSLA', datetime(2018, 11, 22, 10, 4, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
        ]
    }

class TheEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, Stock) or isinstance(arg, Trade):
            result = arg.as_dict()
            result['object'] = arg.__class__.__name__
            return result
        elif isinstance(arg, Decimal):
            return str(arg)
        elif isinstance(arg, datetime):
            return arg.strftime('%Y-%m-%dT%H-%M-%S')
        elif isinstance(arg, date):
            return arg.strftime('%Y-%m-%d')
        else:
            super().default(arg)

def decode_stock(d):
    s = Stock(d['symbol'],
              datetime.strptime(d['date'], '%Y-%m-%d').date(),
              Decimal(d['open_']),
              Decimal(d['high']),
              Decimal(d['low']),
              Decimal(d['close']),
              int(d['volume'])
              )
    return s
def decode_trade(d):
    s = Trade(d['symbol'],
              datetime.strptime(d['timestamp'], '%Y-%m-%dT%H:%M:%S'),
              d['order'],
              Decimal(d['price']),
              int(d['volume']),
              Decimal(d['commission'])
              )
    return s

def decode_financials(d):
    object_type = d.get('object', None)
    if object_type == 'Stock':
        return decode_stock(d)
    elif object_type == 'Trade':
        return decode_trade(d)
    return d

class TheDecoder(json.JSONDecoder):
    def decode(self, arg):
        data = json.loads(arg)
        return self.parse_financials(data)
    def parse_financials(self, obj):
        if isinstance(obj ,dict):
            obj = decode_financials(obj)
            if isinstance(obj, dict):
                for key, value in obj.items():
                    obj[key] = self.parse_financials(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.parse_financials(item)
        return obj

encoded = json.dumps(activity, cls = TheEncoder)
decoded = json.loads(encoded, cls = TheDecoder)
decoded == activity
