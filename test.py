def changeWords(sentence):
    for char in sentence:
        if char == 'a':
            printSameLine('x')
        elif char == 'bd':
            printSameLine('y')
        else:
            printSameLine(char)

def goWordChange():
    print('')
    print('paste text to change')
    print('')
    text = input()
    print('')
    changeWords(text)
    print('')
    return goWordChange()

goWordChange()