# Coin Flip Streaks
'''
For this exercise, we’ll try doing an experiment. If you flip a coin 100 times and write down an “H” for each heads and “T” for each tails, you’ll create a list that looks like “T T T T H H H H T T.” 

Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails. Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row. As a hint, the function call
  
random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.
'''

import random

print('\n' + '=' * 70 + '\n')

numberOfStreaks = 0
numOfRow = 8
numOfFlip = 100000
htList = []
coinList = ['H', 'T']

# # Code that creates a list of 100 'heads' or 'tails' values.
for experientNumber in range(numOfFlip):
    htList.append(random.choice(coinList) + str(experientNumber))

# Code that checks if there is a streak of 6 heads or tails in a row.
i = 0
while True:
    if i > (numOfFlip-numOfRow):
        break

    streakFlag = 1
    for j in range(numOfRow-1, 0, -1):
        if htList[i][0] != htList[i+j][0]:
            streakFlag = 0
            break

    if streakFlag == 1:
        numberOfStreaks += 1
        print(f"#{numberOfStreaks} Streak Position : {i,i+5}")
        i += numOfRow
        continue

    i += 1

# print(htList)
print(f"\nNumber of Streaks : {numberOfStreaks}")
print(f'Chance of streak : {round(numberOfStreaks / (numOfFlip - numOfRow) * 100, 4)}%')

print('\n' + '=' * 70 + '\n')