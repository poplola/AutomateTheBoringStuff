#2 Dunder/Magic Methods
"""
Python Data Model: https://docs.python.org/3/reference/datamodel.html
"""


# <===== Practice 1:  '__repr__' show the class/function value in memory =====>
print("\n<===== Practice 1: '__repr__' is to print and show the class/function value in memory =====>\n")
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.name})"

    # mutiplication method
    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid argument, must be int.")
        self.name = self.name * x

    # call the function
    def __call__(self, y):
        print("called this function", y)

    # length of variable
    def __len__(self):
        return len(self.name)

p = Person('Tim')
print(p)

# <===== Practice 2:  '__mul__' mutiplication method in class =====>
print("\n<===== Practice 2:  '__mul__' mutiplication method in class =====>\n")
p * 10
print(p)

# <===== Practice 3:  '__call__': called the function =====>
print("\n<===== Practice 3:  '__call__': called the function =====>\n")
p(4)

# <===== Practice 4:  '__len__': length of variable =====>
print("\n<===== Practice 4:  '__len__': length of variable =====>\n")
print(len(p), p)


# <===== Practice 5:  Queue: show queue class code =====>
print("\n<===== Practice 5:  Queue: show queue class code  =====>\n")
from queue import Queue
import inspect

q = Queue()
print(q)
print(inspect.getsource(Queue))


# <===== Practice 6:  '__add__'/'__sub__': how to use queue class methods based on queue class code =====>
print("\n<===== Practice 6:  '__add__'/'__sub__': how to use queue class methods based on queue class code =====>\n")
from queue import Queue as q

class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"

    def __add__(self, item):
        self.put(item)

    def __sub__(self, item):
        self.get()


qu = Queue()
qu + 9
qu + 6
# qu - 2
qu - None

print(qu)


print()