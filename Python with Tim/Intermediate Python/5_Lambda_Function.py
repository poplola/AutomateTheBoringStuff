#5 Lambda Function
# Lambda is a short form of function, create mini function, 
# mini function inside of function
# because mini funtion is only used in that function


# # <===== Practice 1: lambda function =====>
# print("\n<===== Practice 1: lambda function =====>\n")
# def func(x):
#     return x+5

# func2 = lambda x: x+5

# print(func(2))
# print(func2(5))


# # <===== Practice 2: mini function inside of a function  =====>
# print("\n<===== Practice 2: mini function inside of a function  =====>\n")
# def func(x):
#     func2 = lambda x: x + 5
#     return func2(x) +85

# func3 = lambda x, y=3: x + y

# print(func3(3))
# print(func(2))


# <===== Practice 3: lambda inside of map function =====>
print("\n<===== Practice 3: lambda inside of map function =====>\n")
a = [x+1 for x in range(10)]
newList = list(map(lambda x: x + 10, [x+1 for x in range(10)]))
newList2 = list(filter(lambda x: x % 2 == 0, [x+1 for x in range(10)]))
print(newList)
print(newList2)