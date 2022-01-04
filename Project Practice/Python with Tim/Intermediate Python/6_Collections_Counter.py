#6 Collections - counter
# Counter => count the number of items, generate a dictionary
import collections
from collections import Counter

#Containers
#list
#dict
#tuple - inmuttable

#Types
# 1 counter <- this video
# 2 deque
# 3 namedTuple()
# 4 orderDict
# 5 defaultdict

# <===== Practice 1: Counter elements numbers =====>
c = Counter('gallad')
print(dict(c))
c = Counter(['a', 'a', 'b', 'c', 'c'])
print(c)
c = Counter({'a':1, 'b':2})
print(c)
d = Counter(cats=4, dogs=7)
print(c)

# list(c.elements()) ==> all elements in the Counter object
print(list(c.elements()))

# number o fthe most common elemnets in the counter
print(c.most_common(1))

# <===== Practice 2: Counter subtract/update/clear methods. =====>
# c.subtract(d) ==> subtract list d from counter c
c = Counter(a=4, b=2, c=0, d=-2)
d = ['a', 'b', 'b', 'c']    # can be list, set turple, etc.
c.subtract(d)
print(c)
# c.update(d) ==> add list d to conter c
c.update(d)
print(c)
# c.clear() ==> delete all elements in counter c
c.clear()
print(c)

# <===== Practice 3: Counter and Counter '+', '-', '&', '|'. =====>
# c+d / c-d ==> the common elements in counter object c and d to do '+' or '-'
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(['a', 'b', 'b', 'c'])
print(c+d)
print(c-d)

# & / | --> the common elements in counter object c and d to do '&' and return the min/max value
print(c&d)
print(c|d)