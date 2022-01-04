
print('\n=====================================================================\n')

def convertStr(s):
    i = 0
    n = ''
    for m in s:
        if i == (len(s)-1):
            n = n + 'and ' + m
            return n
        else:
            n = n + m + ', '
            i += 1


spam = ['apple', 'banana', 'tofu', 'cats']
# spam1 = []
print(spam, 'convert to a string is : ', convertStr(spam))
print('\n=====================================================================\n')

