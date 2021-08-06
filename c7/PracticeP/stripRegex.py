#! Python3
# stripRegex.py
# Regex Version of the strip() Method
"""
Write a function that takes a string and does the same thing as the strip() string method. 

If no other arguments are passed other than the string to strip, 
then whitespace characters will be removed from the beginning and end of the string. 
Otherwise, the characters specified in the second argument to the function will be removed from the string.
"""

import re

def stripRegex(string, removalChr = ' '):

    print('\n', string)
    print("removalChr : ", removalChr)

    if removalChr == ' ':
        sRegex = re.compile(r'\S+.*\S+')
        mo = sRegex.findall(string)
        print("Result : \n", mo[0])
    else:
        sRegex = re.compile(r'[(%s)]'%{removalChr})    
        mo = sRegex.sub('', text)
        print("Result : \n", mo)


text = "  hello, my name is lisa.   "

stripRegex(text)
stripRegex(text, 'e')