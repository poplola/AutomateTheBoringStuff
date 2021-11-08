#8 Collections - deque
# Deque => 
# A double-ended queue, or deque, has the feature of adding and removing elements from either end. 
# The Deque module is a part of collections library. 
# It has the methods for adding and removing elements which can be invoked directly with arguments.

import collections
from collections import deque

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

# <===== Practice 1:  =====>
d = deque('hello')
print(' #1: ', d)


# <===== Practice 2: append value to list deque from front/end =====>
d.append('4')
d.appendleft(5)
print(' #2: ', d)


# <===== Practice 3: pop the last/first of list item =====>
d.pop()
d.popleft()
print(' #3: ', d)


# <===== Practice 4: clear the deque list =====>
d.clear()
print(' #4: ', d)


# <===== Practice 5: extend the deque list from front/end =====>
d.extend('456')
d.extend('hello')
d.extendleft([1,2,3])   # add item in reverse in front of list
print(' #5: ', d)


# <===== Practice 6: rotate the deque list item from left to right or right to left of list =====>
d.rotate(-2)    # rotate items from front to end of list
print(' #6: ', d)

d.rotate(1)     # # rotate items from end to front of list
print(' #6: ', d)

# <===== Practice 7: maxlen the size of deque list  =====>
d.clear()
d = deque('hello', maxlen=10)
d.append('end')
d.appendleft('left')
d.extend('end')
print(' #7: ', d)
print(' #7: ', d.maxlen)


# <===== Practice 8: reverse the deque =====>
d.reverse()
print(' #8: ', d)