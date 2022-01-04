# Mad Libs 
import re, pyinputplus as pyip

text = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
promptWords = ['ADJECTIVE', 'NOUN', 'VERB', 'NOUN']
mLibs = open('madlibs.txt', 'w')
mLibs.write(text)
mLibs.close()

# promptWords = re.compile(r'\w+')
# mo = promptWords.findall(text)
# print('mo : ', list(mo))
mLibs = open('madlibs.txt', 'a')
mLibs.write('\n\nUpdated by user input: \n')
updatedStr = ''

# replace the words
promptRegex = re.compile(r'\w+|\s|[,.]')
mo = promptRegex.findall(text)
print('mo : ', list(mo))
n = 0
for word in promptWords:
    replaceWord = input(f'\nEnter an {word.lower()}:\n')
    for i in range(n, len(list(mo))):
        if word == mo[i]:
            # mo[i] = replaceWord
            updatedStr += replaceWord
            n = i + 1
            # print('mo : ', list(mo))
            print('updated string : \n', updatedStr)
            break
        else:
            updatedStr += mo[i]

# add the rest of string to updated string
for j in range(n, len(list(mo))):
    updatedStr += mo[j]
        
print('updated string : \n', updatedStr)

# write updated string to file
mLibs.write(updatedStr)
mLibs.close()



