import pyinputplus as pyip

# response = pyip.inputNum('Enter num: ', min=4, lessThan=6)
response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero']) 
print(response)