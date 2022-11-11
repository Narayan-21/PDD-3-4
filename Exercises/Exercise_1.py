from collections import defaultdict
from collections import Counter

d1={'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2={'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3={'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}

def merge_1(*dicts):
    unsorted = defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            unsorted[k] += v
    return dict(sorted(unsorted.items(), key=lambda e: e[1], reverse=True))

print(merge_1(d1,d2,d3))

def merge_2(*dicts):
    unsorted = Counter()
    for d in dicts:
            unsorted.update(d)
    return dict(unsorted.most_common())

print(merge_2(d2,d3))
