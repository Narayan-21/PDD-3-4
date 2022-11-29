def get_item_forgive_me(seq, idx, default=None):
    try:
        return seq[idx]
    except (IndexError, TypeError, KeyError):
        return default

def get_item_ask_perm(seq, idx, default=None):
    if hasattr(seq, '__getitem__'):
        if idx < len(seq):
            return seq[idx]
    return default

print(get_item_forgive_me([1,2,3],10,'Nope'))
print(get_item_ask_perm([1,2,3],2,'Nope'))

# Although both the get_item_forgive_me and get_item_ask_perm looks same here, but they are not.
# We can use 'get_item_forgive_me' function for both list and dictionary since we are looking at
# generalised properties. But in the 'get_item_ask_perm' function we are restraining ourselves to
# the specific properties eg __getitem__.

print(get_item_forgive_me({'a': 100}, 'a'))
print(get_item_ask_perm({'a': 100}, 'a'))
