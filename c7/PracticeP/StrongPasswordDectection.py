#! Pyhton3 
# StrongPasswordDectection.py
# Strong Password Detection
"""
Write a function that uses regular expressions to make sure the password string it is passed is strong. 

A strong password is defined as one that is 
    at least eight characters long, 
    contains both uppercase and lowercase characters, 
    and has at least one digit. 

You may need to test the string against multiple regex patterns to validate its strength.
"""

import re

password = input("Please enter password : ")

# passwordRegex = re.compile(r'([a-z]+[A-Z]+\d+(.*)+?){8,}')
# passwordRegex = re.compile(r'([a-z]+[A-Z]+\d+.*){8,}')
passwordRegex = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[ #?!@$%^&*-]).{8,}$")

mo = passwordRegex.search(password)

if mo == None:
    print(f'\nYour Password <{password}> is NOT STRONG!\n')
else:
    print(f'\n===== Congratulations! Your Password <{password}> is STRONG! =====\n')
