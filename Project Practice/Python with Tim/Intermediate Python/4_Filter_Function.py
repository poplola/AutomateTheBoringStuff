#4 Filter Funtion
#  filter parameter takes function and iterable list 


# <===== Practice 1: filter items in list based on the function =====>

def add7(x):
    return x+7

def isOdd(x):
    return x%2 != 0
    # return 'hi'
    # return True
    # return 0
    # return False

a = [1,2,3,4,5,6,7,8,9,10]
print(a)

print("\n<===== Practice 1: filter items in list based on the function =====>")
b = list(filter(isOdd, a))
print(" #1: ", b)


# <===== Practice 2: use map function  =====>
print("\n<===== Practice 2: use map function  =====>")
c = list(map(add7, filter(isOdd,a)))
print(" #2: ", c)