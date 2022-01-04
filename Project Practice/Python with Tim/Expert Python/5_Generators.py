#4 Generators
"""
To create a mess of big values, think if you really need all of those values?
probably you just need to remember last value, a few values. so use generate for faster program.
To let the code to access the data in memory to run faster than accessing hard drive.
Generator is not to create a list of number, it's to remeber last number of generated.

Practice 1: reglar way to create a buge number of list (not working)
Practice 2: create a generator pattern class / remember the last number that generated
Practice 3: 'yield' is to pause function / 'return' like stop function
Practice 4: memory size that generator and list take
"""


# # <===== Practice 1: reglar way to create a buge number of list (not working)  =====>
# print("\n<===== Practice 1: reglar way to create a buge number of list (not working) =====>\n")
# x = [i**2 for i in range(10000000000)]

# # for el in x:
# #     print(el)

# for i in range(10000000000):
#     print(i**2)


# # <===== Practice 2: create a generator pattern class / remember the last number that generated =====>
# print("\n<===== Practice 2: *args, **kwargs / pass function as a function parameter=====>\n")
# class Gen:
#     def __init__(self, n):
#         self.n = n
#         self.last = 0

#     # The __next__() method must return the next item in the sequence. 
#     # On reaching the end, and in subsequent calls, it must raise StopIteration .
#     def __next__(self):
#         return self.next()

#     def next(self):
#         if self.last == self.n:
#             raise StopIteration()
        
#         rv = self.last ** 2
#         self.last += 1
#         return rv

# g = Gen(10)

# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break


# # <===== Practice 3: 'yield' is to pause function / 'return' like stop function =====>
# print("\n<===== Practice 3: 'yield' is to pause function / 'return' like stop function =====>\n")
# def gen(n):
#     for i in range(n):
#         yield i**2      # 'yield' is to pause the code

# def gen1(m):
#     yield 1
#     yield 10
#     yield 100
#     yield 1000
#     yield 10000

# g = gen(100)

# # for i in g:
# #     print(i)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print()

# g1 = gen1(1000000)
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))     # out of 1000000 range and caused 'StopIteration' exception


# <===== Practice 4: memory size that generator and list take =====>
print("\n<===== Practice 4: memory size that generator and list take  =====>\n")
import sys

def gen(n):
    for i in range(n):
        yield i**2

x = [i ** 2 for i in range(10000)]
g = gen(10000)

print(sys.getsizeof(x))
print(sys.getsizeof(g))




print()