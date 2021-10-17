#5 Lambda Function
# Lambda is a short form of function, create mini function, 
# function inside of function

# # ==================================== 1 =====
# def func(x):
#     return x+5

# func2 = lambda x: x+5

# print(func(2))
# print(func2(5))


# # ==================================== 2 =====
# def func(x):
#     func2 = lambda x: x + 5
#     return func2(x) +85

# func3 = lambda x, y=3: x + y

# print(func3(3))
# print(func(2))


# # ==================================== 3 =====
# a = [x+1 for x in range(10)]
newList = list(map(lambda x: x + 10, [x+1 for x in range(10)]))
newList2 = list(filter(lambda x: x % 2 == 0, [x+1 for x in range(10)]))
print(newList)
print(newList2)