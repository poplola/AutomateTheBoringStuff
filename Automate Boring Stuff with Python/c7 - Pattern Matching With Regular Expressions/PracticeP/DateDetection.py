#! python3
# DateDectection.py
# Date Detection
"""
Write a regular expression that can detect dates in the DD/MM/YYYY format. 
    Assume that the days range from 01 to 31, 
    the months range from 01 to 12, 
    and the years range from 1000 to 2999. 
    Note that if the day or month is a single digit, it’ll have a leading zero.

The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. 

Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. 
    April, June, September, and November have 30 days, 
    February has 28 days, 
    and the rest of the months have 31 days. 
    February has 29 days in leap years. 
    Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. 

Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.
"""

import re

text = "The regular expression 01/2/2999 doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. April, June, September, 29/02/2040 and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days i"

dateRegex = re.compile(r'\s(0?[1-9]|[12]\d|3[01])\/(0?[1-9]|1[012])\/([12]\d{3})')
mo = dateRegex.findall(text)
print(mo)

formattedDate = []
for group in mo:
    # print(group)
    day, month, year = group
    # print(day, month, year)
    dayInt = int(day)
    monthInt = int(month)
    yearInt = int(year)

    if monthInt in [4, 6, 9, 11] and dayInt <= 30 or \
    monthInt in [1, 3, 5, 7, 8, 10, 12] and dayInt <= 31 or \
    monthInt in [2] and dayInt <= 28 or \
    monthInt in [2] and dayInt == 29 and not(yearInt % 4) and (yearInt % 100 or yearInt % 400):
        print(f"{day.rjust(2,'0')}/{month.rjust(2,'0')}/{year}")

