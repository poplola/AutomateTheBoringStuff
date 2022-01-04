
import pyperclip, re

print('\n=====================================================================\n')

# Create Date Regex in DD/MM/YYYY
dateRegex = re.compile(r'''(
    # (3[0-1]|[12][0-9]|[1-9])      # DD
    ([1-9]|[123][0-9])
    # (\s|/|-|.)                  # separator
    [/.-]
    # ^([1-9]|1[012])$            # MM
    (1[0-2]|[1-9])
    # (\s|/|-|.)                  # separator
    [/.-]
    ([12]\d\d\d)                 # YYYY
    )''', re.VERBOSE)

# dateRegex = re.compile(r'\d{1,2}[/.-]\d{1,2}[/.-]\d{4}')
text = '''2/3/2010, 32/12/2099
    Fdsafdsa. 9/9/1990,dssf dslj
    03/12/1991
    35/9/2000
        '''

# text = str(pyperclip.paste())
print('text is : \n', text)
print()
# month = 0
# day = 0
# year = 0

# print('find all text : ', dateRegex.findall(text))
for group in dateRegex.findall(text):

    # print('group : \n', group)
    # print('dateRegex.findall: \n', dateRegex.findall(text))
    # c = ''
    # n = 0
    # for i in group:
    #     if i != '/' :
    #        c += i
    #     else:
    #         c = ''
    #         n += 1
        
    #     if n == 0:
    #         day = c
    #     elif n == 1:
    #         month = c
    #     else:
    #         year = c

    # print('group 1 : ', group[0])

    
    day = int(group[1])
    month = int(group[2])
    year = int(group[3])


    if day>=1 and day <=31 and month>=1 and month<=12 and year>=1000 and year <=2999:
        print('\nValide Date found : ', group[0])


    # if len(group[2]) == 1:
    #     group[2] == '0' + group[2]
    # day = int(group[1])
    # print('group 1 updated: ', group[1])
    # print('day and type: \n', day, type(day))
    # print('month and type : \n', month, type(month))
    # print('year anbd type: \n', year, type(year))
    print()

print('\n=====================================================================\n')