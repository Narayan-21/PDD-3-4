# 1.Sorting the dictionary by values.

def sort_dict_by_value(d):
    d={k:v for k, v in sorted(d.items(), key=lambda e:e[1])}
    return d

Dict = {'a':1,'f':20,'c':8,'d':9,'b':3,'e':12}
print(sort_dict_by_value(Dict))


# 2. Finding keys common to both given dictionaries and making the tuple as the values.
d1 = {'a':1, 'b':2, 'c':3, 'd':4}
d2 = {'b':20, 'c':30, 'y':40, 'z':50}

def intersect(d1,d2):
    d1_keys = d1.keys()
    d2_keys = d2.keys()
    keys = d1_keys & d2_keys
    d={k: (d1[k],d2[k]) for k in keys}
    return d

print(intersect(d1,d2))

# 3. Generating one dictionary out of three given with values being the sum of all three values of respective keys

d1 = {'python': 10, 'java':3, 'c#':8, 'javascript':15}
d2 = {'java': 10, 'c++':10, 'c#':4, 'go':9, 'python':6}
d3 = {'erlang': 5, 'haskell':3, 'python':1, 'pascal':1}

def func(*dicts):
    unsorted = {}
    for d in dicts:
        for k,v in d.items():
                 unsorted[k] = unsorted.get(k,0) + v
    return unsorted

print(func(d1,d2,d3))


# 4. Filtering the dictionaries based on keys not existing in all dictionaries.

n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
n2 = {'employees': 250, 'users': 23, 'user': 230}
n3 = {'employees': 150, 'users': 4, 'login': 1000}

union = n1.keys() | n2.keys() | n3.keys()
intersection = n1.keys() & n2.keys() & n3.keys()
def identity(node1, node2, node3):
    union = node1.keys() | node2.keys() | node3.keys()
    intersection = node1.keys() & node2.keys() & node3.keys()
    relevant = union - intersection
    result = {
        key: (node1.get(key,0), node2.get(key,0), node3.get(key,0))
        for key in relevant
        }
    return result

print(identity(n1,n2,n3))
