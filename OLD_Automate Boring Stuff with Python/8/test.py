
import pyinputplus as pyip
# totalCost = 12.50

# print('Total Price :', '${:,.2f}'.format(totalCost))

priceList = {'Wheat':1, 'White':1, 'Sourdough':1,
             'Chicken':2, 'Turkey':2.5, 'Ham':3, 'Tofu':1,
             'Cheddar':0.5, 'Swiss':0.5, 'Mozzarella':1,
             'Mayo': 0.25, 'Mustard':0.25, 'Lettuce':0.5, 'Tomato':0.5
            }
# totalCost = int(priceList[choiceBread]) + int(priceList[choiceProtein]) + int(priceList[choiceCheese]) + int(priceList[choiceMustard] + int(priceList[choiceMustard])
#             + int(priceList[choiceLettuce]) + int(priceList[choiceTomato])


# Using inputMenu() for a bread type: wheat, white, or sourdough.
# choiceBread = pyip.inputMenu(['wheat '.ljust(20, '-')+' $1.00', 'White '.ljust(20, '-')+' $1.00', 'Sourdough '.ljust(20, '-')+' $1.00'], numbered=True)
# choiceProtein = pyip.inputMenu(['Chicken '.ljust(20, '-')+' $2.00', 'Turkey '.ljust(20, '-')+' $2.50', 'Ham '.ljust(20, '-')+' $3.00', 'Tofu '.ljust(20, '-')+' $1.00'], numbered=True)
choiceCheese = pyip.inputMenu(['Cheddar '.ljust(20, '-')+' $0.50', 'Swiss '.ljust(20, '-')+' $0.50', 'Mozzarella '.ljust(20, '-')+' $1.00'], numbered=True)

print('\nchoice of Bread : %s\n'%(choiceBread))


totalCost = priceList['Wheat'] + priceList['Swiss']
# print(priceList['Wheat'])

totalCost = totalCost * 2

print('Total Price : ', '${:,.2f}'.format(totalCost))

print('='*100+'\n'*2)