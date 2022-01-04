import pyinputplus as pyip

print('\n'+'='*100+'\n')

prompt = '\nWant to know how to keep an idiot busy for hours?\n'

response = pyip.inputYesNo(prompt)

while response == 'yes':
    print('To be continued ... ...')
    break

print('Thank you! Have a nice day!')

print('\n'+'='*100+'\n')