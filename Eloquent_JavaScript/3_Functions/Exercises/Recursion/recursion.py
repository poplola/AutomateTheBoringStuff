"""
Recursion
We’ve seen that % (the remainder operator) can be used to test whether a number is even or odd by using % 2 to see whether it’s divisible by two. 
Here’s another way to define whether a positive whole number is even or odd:
• Zero is even.
• One is odd.
• For any other number N, its evenness is the same as N - 2.
Define a recursive function isEven corresponding to this description. 
The function should accept a single parameter (a positive, whole number) and return a Boolean.
Test it on 50 and 75. See how it behaves on -1. Why? Can you think of a way to fix this?
"""

from operator import truediv


def isEven(num):
    if num < 0:
        return None
    if num == 0:
        return True
    elif num == 1:
        return False
    else:
        return isEven( num - 2 )

checkNumber = 75
if (isEven(checkNumber) == None):
    print(f"{checkNumber} is a negtive number. Please give a positive number to check even or odd.")
elif (isEven(checkNumber)):
    print(f"{checkNumber} is even number.")
else:
    print(f"{checkNumber} is odd number.")