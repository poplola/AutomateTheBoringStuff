#1 Overview of Python
"""
cool feathers in python.
    1: Understand compiler and interpreter.
    2: define a function in a for loop 
    3: define function inside of function.
    4: use instance id showing function memory location 
    5: instpect module: get inspect doc of function in memory
    6: instpect module: check the source code when access class/function
    7: Queue module
"""


# <===== Practice 1: compiler and interpreter =====>
print("\n<===== Practice 1: compiler and interpreter =====>\n")
def make_class(x):
    class Dog:
        def __init__(self, name):
            self.name = name

        def print_value(self):
            print(x)

    return Dog

cls = make_class(10)
d = cls("Tim")
print(d.name)
d.print_value()

# <===== Practice 2: define a function in a for loop  =====>
print("\n<===== Practice 2: define a function in a for loop  =====>\n")
for i in range(10):
    def show():
        print(i*2)
    show()
print()
show()

# <===== Practice 3: define function inside of function =====>
print("\n<===== Practice 3: define function inside of function. =====>")
print("<===== To choose to use which function based on condition. =====>\n")

def func(x):
    if x==1:
        def rv():
            print("X is equal to 1.")
    else:
        def rv():
            print("X is not 1.")
    return rv
new_func = func(2)
new_func()

# <===== Practice 4: use instance id showing memory location =====>
print("\n<===== Practice 4: use instance id showing function memory location =====>\n")
print(id(new_func()))


# <===== Practice 5: instpect module: get inspect doc of function in memory =====>
print("\n<===== Practice 5: instpect module: get inspect doc of function in memory =====>\n")
import inspect
# print(inspect.getmembers(new_func))
for item in inspect.getmembers(new_func):
    print(item)

# <===== Practice 6: instpect module: check the source code when access class/function =====>
print("\n<===== Practice 6: instpect module: check the source code when access class/function =====>\n")
print(inspect.getsource(new_func))


# <===== Practice 7: Queue module : build in queue class data structure in python  =====>
print("\n<===== Practice 7: Queue module : build in queue class data structure in python =====>\n")
from queue import Queue
print(inspect.getsource(Queue))


print()