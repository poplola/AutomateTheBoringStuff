import pyinputplus as pyip

prompt = 'Want to know how to keep an idiot busy for hours?'

answer = 'yes'

while answer == 'yes':
    answer = pyip.inputYesNo(prompt)

print('Thank you. Have a nice day!')