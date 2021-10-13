import random

print('\n=====================================================================\n')

numberOfStreaks = 0
numberOfHeadOrTail = 0
count = 100000          # Number of list items, loop times
headTailList= []
preValue = ''
x = 17       # 6 times of head or tail counted as one time streak

for experientNumber in range(count):

    # Part 1 : Code that creat a list of 100 'heads' or 'tails' values.
    headTailList.append(random.choice(['H','T']))
    # print(f'{experientNumber} : {headTailList[experientNumber]}')


    # Part 2 : Code that checks if there is a streak of 6 heads or tails in a row.
    if headTailList[experientNumber] == preValue:
        numberOfHeadOrTail += 1
    else:
        numberOfHeadOrTail = 1
    
    if numberOfHeadOrTail == x:
        numberOfStreaks += 1
    
    preValue = headTailList[experientNumber]

print(f'Total flip coin times is : {count}\n')

print(numberOfStreaks, f'streaks of {x} heads or {x} tails of coin!\n')

print('Chance of streak: %s%%'%(numberOfStreaks/count))

print('\n=====================================================================\n')