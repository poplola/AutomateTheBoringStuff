import re, sys




def passwordStrength(psd):
    print('\n=====================================================================\n')
    print('password is : ', psd)
    # if len(psd) < 8:
    #     print('\nWeak Password! The password is less than 8 character!\n')
    #     print(f"It's only {len(psd)} character.")
    #     sys.exit()
    # psdRegex = re.compile(r'[a-z]+[A-Z]+|[0-9]{1,}')
    psdRegex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$')
    mo = psdRegex.findall(psd)

    print('mo group: ', mo)

    if len(psd) < 8:
        print('\nWeak Password! The password is less than 8 character!')
        print(f"It's only {len(psd)} character.\n")
        sys.exit()
    elif mo == []:
        print('\nWeak Password! \nThe password should contain both upper case and lower case, and at least 1 digital number.')
        sys.exit()
    
    print('\nThe password is STRONG! \n\nGOOD JOB!')


    print('\n=====================================================================\n')

def main():
    password = 'kFFF5FFFFF'
    passwordStrength(password)



if __name__ == "__main__": main()

