import string
from itertools import chain

text = 'Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit amet consectetur adipisci[ng] velit, sed quia non-numquam [do] eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?'

def cat_key(c):
    if c== ' ':
        return None
    elif c in string.ascii_lowercase:
        return 'lower'
    elif c in string.ascii_uppercase:
        return 'upper'
    else:
        return 'other'

categories = {}
for c in text:
    key = cat_key(c)
    if key:
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}: ', ''.join(categories[cat]))

def cat_key(c):
    cat1 = {' ': None}
    cat2 = dict.fromkeys(string.ascii_lowercase, 'lower')
    cat3 = dict.fromkeys(string.ascii_uppercase, 'upper')
    categories = dict(chain(cat1.items(), cat2.items(), cat3.items()))
    # o.w. {**cat1, **cat2, **cat3}
    return categories.get(c, 'other')

print(cat_key('a'), cat_key('G'), cat_key(':'), cat_key(' '))
