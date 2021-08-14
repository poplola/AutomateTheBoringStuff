#! Python3
# Sandwich Maker
"""
Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:
    Using inputMenu() for a bread type: wheat, white, or sourdough. 
    Using inputMenu() for a protein type: chicken, turkey, ham, or tofu. 
    Using inputYesNo() to ask if they want cheese.
        If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella. 
    Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
    Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
"""

import pyinputplus as pyip

# format program title
print('\n'*2) 
print("="*70)
print("     Welcome to Sandwich Maker!     ".center(70, '='))
print("=" * 70 + '\n')

breadDic = {'Wheat': 1, "White": 2, "Sourdough": 3}
proteinDic = {'chicken': 1, 'turkey': 2, 'ham': 3, 'tofu': 4}
cheeseDic = {'cheddar': 1, 'swiss': 2, 'mozzarella': 3}
otherDic = {'mayo': 1, 'mustard': 2, 'lettuce': 3, 'tomato': 4}
cheeseChoice = ''
total = 0.0
orderList = []

breadChoice = pyip.inputMenu(list(breadDic.keys()), numbered=True)
total += breadDic[breadChoice]
orderList.append(breadChoice) 
print(f"\nYour chose bread type : {breadChoice} (${breadDic[breadChoice]})")
print(f"Total : ${total}\n")

proteinChoice = pyip.inputMenu(list(proteinDic.keys()), numbered=True)
orderList.append(proteinChoice) 
# orderStr += ' ' + (proteinChoice)
total += proteinDic[proteinChoice]
print(f"\nYour chose protein type : {proteinChoice} (${proteinDic[proteinChoice]})")
print(f"Total : ${total}\n")


if (pyip.inputYesNo('Do you want cheese? ') == 'yes'):
    cheeseChoice = pyip.inputMenu(list(cheeseDic.keys()), numbered=True)
    orderList.append(cheeseChoice) 
    # orderStr += ' ' + (cheeseChoice)
    total += cheeseDic[cheeseChoice]
    print(f"\nYour chose cheese type : {cheeseChoice} (${cheeseDic[cheeseChoice]})")
    print(f"Total : ${total}\n")


if (pyip.inputYesNo('Do you want mayo, mustard, lettuce, or tomato?') == 'yes'):
    otherChoice = pyip.inputMenu(list(otherDic.keys()), numbered=True)
    orderList.append(otherChoice) 
    # orderStr += ' ' + (otherChoice)
    total += otherDic[otherChoice]
    print(f"\nYour chose : {otherChoice} (${otherDic[otherChoice]})\n")
    print(f"Total : ${total}\n")



count = pyip.inputInt("\nHow many sandwiches do you want?  ", min=1)
total *= count
print(f"Total : ${total}\n")
orderList[-1] = 'and ' + orderList[-1]


print(" Your Order Summery ".center(66, '='))
print(f"\nYou have ordered {count} sandwich(es), each sandwich includes: {', '.join(orderList)}\n")
print(f"Total : ${total}\n")
print(f" Thank you for shopping in Sandwich Maker! ".center(66, '='))
print('\n'* 2)