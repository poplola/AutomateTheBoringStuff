import re

print('\n' + '='*100 + '\n')


def reStrip(textStr, remove_c):
    print(f"text = '{textStr}'")
    print(f'remove_c = {remove_c}')
    if remove_c == '':
        # spaceRegex = re.compile(r'[^[ ]+|[.*]+|^[ ]+$]', re.DOTALL)
        # spaceRegex = re.compile(r'[^[ ]+|^[ ]+$]', re.DOTALL)
        spaceRegex = re.compile(r'[^[ ]+')

        # mo = spaceRegex.findall(textStr)
        mo = spaceRegex.findall(textStr)
        mo = ' '.join(mo)
        # regroupMo = mo.groups()
        print(f"mo strip: '{mo}'")
        print(f'lengh of mo : {len(mo)}')
        print(f'lengh of text : {len(textStr)}')
    else:
        cRegex = re.compile(remove_c)
        mo = cRegex.sub('', textStr)
        print(f"mo remove '{remove_c}' : '{mo}'")
        
    print('\n' + '='*100 + '\n')



def main():
    
    text = '   we are learning python!    '
    
    removeCharacter = 'a'
    
    reStrip(text, removeCharacter)



if __name__ == "__main__": main()