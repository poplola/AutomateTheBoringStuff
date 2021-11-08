#3 Metaclasses
"""
use 'Type' function to create a class
"""


# <===== Practice 1:  type of class / type of class instance =====>
print("\n<===== Practice 1:  type of class / type of class instance or object =====>\n")
class Test:
    pass

def func():
    pass

print(Test)
print(type(Test))
print(Test())
print(type(Test()))
print(type(2))
print(type(func))


# <===== Practice 2: Test1 = type('Test1', (), {}) : another way to de fine class =====>
print("\n<===== Practice 2: Test1 = type(class name, bases, attrs) : use 'Type' function to create a class =====>\n")
Test2 = type('Test', (), {"x": 5})
print(Test2)
t = Test2()
print(t.x)
t.wy = 'hello'
print(t.wy)

# <===== Practice 3: inherance from class / add attribute =====>
print("\n<===== Practice 3: inherance from class / add attribute =====>\n")
class Foo:
    def show(self):
        print('hi')

def add_attribute(self):
    self.z = 9

Test3 = type('Test', (Foo,), {"x":5, "add_attribute":add_attribute})
t = Test3()
t.show()
t.add_attribute()
print(t.z)

# <===== Practice 4:  Meta class inherance from type =====>
print("\n<===== Practice 4:  Meta class inherance from type =====>\n")
class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        # print(class_name)
        # print(bases)
        a = {}
        for name, val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val
        print(a)
        # return type(class_name, bases, attrs)
        return type(class_name, bases, a)

class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("hi")

d = Dog()
print(d.X)



# # <===== Practice 5:  Queue: show queue class code =====>
# print("\n<===== Practice 5:  Queue: show queue class code  =====>\n")
# from queue import Queue
# import inspect

# q = Queue()
# print(q)
# print(inspect.getsource(Queue))


# # <===== Practice 6:  '__add__'/'__sub__': how to use queue class methods based on queue class code =====>
# print("\n<===== Practice 6:  '__add__'/'__sub__': how to use queue class methods based on queue class code =====>\n")
# from queue import Queue as q

# class Queue(q):
#     def __repr__(self):
#         return f"Queue({self._qsize()})"

#     def __add__(self, item):
#         self.put(item)

#     def __sub__(self, item):
#         self.get()


# qu = Queue()
# qu + 9
# qu + 6
# # qu - 2
# qu - None

# print(qu)


print()