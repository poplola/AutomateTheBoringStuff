#! Python3
# 
"""
PyInputPlus’s features can be useful for creating a timed multiplication quiz. 
By setting the allowRegexes, blockRegexes, timeout, and limit keyword argument to pyip.inputStr(), you can leave most of the implementation to PyInputPlus.
Let’s create a program that poses 10 multiplication problems to the user, where the valid input is the problem’s correct answer. 
    We’ll import pyinputplus, random, and time. 
    We’ll keep track of how many questions the program asks 
    and how many correct answers the user gives with the variables numberOfQuestions and correctAnswers. 
    A for loop will repeatedly pose a random multiplication problem 10 times:
"""

import pyinputplus as pyip
import random, time

times = 5
numList = []
correctNum = 0
defaultPrompt = " '❌' Failed because of over 5 seconds answering question!\n"

for i in range(times):
    numList = [random.randint(1, 10) for i in range(2)]
    print(f"# {i+1} : \n{numList[0]} X {numList[1]} = ", end='')
    answer = pyip.inputInt(timeout=5, default=defaultPrompt)
    if answer == defaultPrompt:
        print(answer)
        continue

    if answer == (numList[0] * numList[1]):
        correctNum += 1
        print("'✅' Passed!\n")
        continue
    else:
        print("'❌' Failed! Wrong answer!\n")

print(f"\n======== You got {correctNum} of {times} question(s) correct. ========\n")

