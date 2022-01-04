#4 Decorators
"""
Decorators can change the functions behavior, is to validate or check function
function is an object in python
decorator function is two funtion:
    1. the first function's parameter is a function
    2. the second function is wrapper() function, it will be called and return wrapper in first function

Practice 1: return a function inside of a function
Practice 2: *args, **kwargs / pass function as a function parameter
Practice 3: how to use decorator '@functionName' / pass args
Practice 4: @timer decorator : check how fast the function code run
"""


# <===== Practice 1: return a function inside of a function =====>
print("\n<===== Practice 1: return a function inside of a function =====>\n")
def func(string):
    def wrapper():  # wrapper function has the same number of arguments that function called
        print("Started")
        print(string)
        print("Ended")
    # return wrapper()    # return wrapper() function
    return wrapper    # nothing in output because wrapper is not function

x = func("hello")   # call wrapper function
print(x)    # print function address when return wrapper
x()     # x() is to call 'wrapper()' function



# <===== Practice 2: *args, **kwargs / pass function as a function parameter =====>
print("\n<===== Practice 2: *args, **kwargs / pass function as a function parameter=====>\n")
# func function below is a decorator function
def func(f):
    def wrapper(*args, **kwargs):   # *args, **kwargs ==> accept all the args pass in
        print("\nStarted")
        rv = f(*args, **kwargs)
        print("Ended")
        return rv
    # return wrapper()    # return wrapper() function
    return wrapper    # nothing in output because wrapper is not function

@func   # equal to code line : func2 = func(func2) in practice 3
def func2(x, y):
    print(f"I am func 2. Function parameter is : {x} {y}.")
    return y

@func   # equal to code line : func3 = func(func3) in practice 3
def func3():
    print("I am func 3.")

x = func(func2)   # call wrapper function
y = func(func3)
print(x)    # print function address when return wrapper
x(5,9)     # x() is to call 'wrapper()' function
y()



# <===== Practice 3: how to use decorator '@functionName' / pass args =====>
print("\n<===== Practice 3: how to use decorator '@functionName' / pass args =====>\n")
# func2 = func(func2)     # func2 = func(func2) equal to @func decorator above func2
# func3 = func(func3)     # func3 = func(func3) equal to @func decorator above func3
x = func2(2, 9)
func3()
print(x)



# <===== Practice 4: Timer decorator : check how fast the code run =====>
print("\n<===== Practice 4: Timer decorator : check how fast the code run =====>\n")
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        # rv = func()
        func()
        total = time.time() - start
        print(f"Total run time: {total} seconds.")
        # return rv
    return wrapper

@timer
def test():
    for _ in range(10000000):
        pass
    return print('hi')

@timer
def test2():
    time.sleep(1)

test()
test2()

# # my own program
# import time

# def timer(func):
#     def wrapper():
#         start = time.time()
#         func()
#         total = time.time() - start
#         print()
#         print(' '.join(str(func)[1:].split(' ')[:2]))
#         print(f"total run seconds : {total}")
#     return wrapper


# @timer
# def test1():
#     for _ in range(1000000):
#         pass


# @timer
# def test2():
#     for _ in range(10000000):
#         pass


# test1()
# test2()

print()