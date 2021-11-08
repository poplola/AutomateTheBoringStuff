#7 Collections - named tuple
# Named Tuple => is a factory function available in collections . 
#                It allows you to create tuple subclasses with named fields.

import collections
from collections import namedtuple

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
Point = namedtuple('Point', 'x y z')
# Point = namedtuple('Point', ['x', 'y', 'z'])  # can be list
# Point = namedtuple('Point', {'x': 0, 'y':0 , 'z': 0})  # can be list
# Point = namedtuple('Point', 'x gy z h')   # can add more variables
# newP = Point(3, 4, 5, 9)  # more variable, the same number of value to match

newP = Point(3, 4, 5)
print(" #1 :", newP)    # # print named tuple

print(" #2 :", newP.x, newP.y, newP.z)  # print named tuple values

print(" #3 :", newP[0], newP[1], newP[2])   # print named tuple values

print(" #4 :", newP._asdict())  # print named tuple as dictionary

print(" #5 :", newP._fields)    # print variable names

newP = newP._replace(y=10)  # assign new value to variable
print(" #6 :", newP)

P2 = Point._make(['a', 'b', 'c'])   # assign new value to named tuple
print(" #7 :", P2)

