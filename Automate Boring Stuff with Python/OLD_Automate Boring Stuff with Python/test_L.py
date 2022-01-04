import random, sys, copy

# n = random.randint(1, 20)
# print('I am thinking of a number between 1 to 20')

# while True:
#     m = int(input("Take a guess! "))
#     if m < n:
#         print('Your number is LOW!')
#     elif m >n:
#         print('Your number is HIGH!')
#     else:
#         print(f"Good Job! you guessed right! It's {m}.")
#         break

# print('range(10) : ', list(range(10)))
# print('range(0, 10) : ', list(range(0, 10)))
# print('range(0, 10, 1) : ', list(range(0, 10, 1)))
# print(round(5.67))


# def spam(divideBy):
#     try:
#         return 50 / divideBy
#         # print(f"50 / {divideBy} = ", y)
#     except ZeroDivisionError:
#         print('Invalid argument!')

# print(spam(2))
# print(spam(0))

# message = ['a', 'b', 'c', 'd', 'e', 'f']

# print(message[random.randint(0, len(message)-1)])
# print(random.choice(message))
# print(33//11)

# a = [1, 2, 3]
# b = copy.copy(a)
# d= a.index
# c = copy.deepcopy(a)
# print('a id is ', id(a))
# print('b id is ', id(b))
# print('c id is ', id(c))
# print('d id is ', d)

a = 'as.txt'
b = '.txt'
if b in a:
    print(a)