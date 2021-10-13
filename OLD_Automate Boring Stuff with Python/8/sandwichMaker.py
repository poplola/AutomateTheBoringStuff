import pyinputplus as pyip

# Print title
title = '||   WELCOME TO SANDWICH MAKER   ||'
print('\n'*2+'='*len(title))
print(title)
print('='*len(title)+'\n'*2)


priceList = {'Wheat':1, 'White':1, 'Sourdough':1,
             'Chicken':2, 'Turkey':2.5, 'Ham':3, 'Tofu':1,
             'Cheddar':0.5, 'Swiss':0.5, 'Mozzarella':1,
             'Mayo': 0.25, 'Mustard':0.25, 'Lettuce':0.5, 'Tomato':0.5,
             '':0
            }

totalCost = 0
choiceCheese = ''
choiceMayo = ''
choiceMustard = ''
choiceLettuce = ''
choiceTomato = ''


# Using inputMenu() for a bread type: wheat, white, or sourdough.
choiceBread = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], numbered=True)
print('\nchoice of Bread : %s\n'%(choiceBread))

# Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
choiceProtein = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered=True)
print('\nchoice of protein : %s\n'%(choiceProtein))

# Using inputYesNo() to ask if they want cheese.
promptCheese = 'Do you want cheese?'
ynCheese = pyip.inputYesNo(promptCheese)
print('\nwant cheese?  %s\n'%(ynCheese))

# If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
if ynCheese == 'yes':
    choiceCheese = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], numbered=True)
    print('\nchoice of cheese : %s\n'%(choiceCheese))

# Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
prompt = 'Do you want '
ynMayo = pyip.inputYesNo(prompt+'mayo?')
if ynMayo == 'yes':
    choiceMayo = 'Mayo' 
print('\nYou want:  %s\n'%(choiceMayo))



# prompMustard = 'Do you want mustard?'
ynMustard = pyip.inputYesNo(prompt+'mustard?')
if ynMustard == 'yes':
    choiceMustard = 'Mustard' 
print('\nYou want :  %s\n'%(choiceMustard))



# prompL = 'Do you want lettuce?'
ynLettuce = pyip.inputYesNo(prompt+'lettuce?')
if ynLettuce == 'yes':
    choiceLettuce = 'Lettuce' 
print('\nYou want :  %s\n'%(choiceLettuce))



# prompT = 'Do you want tomato?'
ynTomato = pyip.inputYesNo(prompt+'tomato?')
if ynTomato == 'yes':
    choiceTomato = 'Tomato' 
print('\nYou want :  %s\n'%(choiceTomato))
    



# Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
prompt = 'How many sandwiches do you want? '
count = pyip.inputInt(prompt, min=1)

print('='*len(title)+'\n'*2)

print('\nYou ordered %s sandwish(es), including: %s bread with %s inside, and %s %s %s %s %s '
        %(str(count), choiceBread, choiceProtein, choiceCheese, choiceMayo, choiceMustard, choiceLettuce, choiceTomato))



totalCost = (priceList[choiceBread] + priceList[choiceProtein] + priceList[choiceCheese] + priceList[choiceMustard] + priceList[choiceMustard]
            + priceList[choiceLettuce] + priceList[choiceTomato]) * count
    

# totalCost = totalCost * count

print('Total Price : ', '${:,.2f}'.format(totalCost))

print('='*len(title)+'\n'*2)
