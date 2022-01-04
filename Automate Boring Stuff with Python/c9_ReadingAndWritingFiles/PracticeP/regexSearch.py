#! Python 3
# Regex Search
# regexSearch.py
"""
Write a program that opens all .txt files in a folder 
and searches for any line that matches a user-supplied regular expression. 
The results should be printed to the screen.
"""

from pathlib import Path
import os, re

def matchPrint(ItemList, fileName, matchItem):
    print(f"\n\t{len(ItemList)} {matchItem} found.")
    if ItemList:
        for item in ItemList:
            print(f'\t\t{item}')

folder = Path('./c9_ReadingAndWritingFiles/PracticeP/regexSearch')
# print("folder = " , folder)

filesList = os.listdir(folder)
filesList.sort()

for file in filesList:
    # print("file = " , file)
    fileText = open(folder / file)
    textStr = fileText.read()
    # print(textStr)
    print(f"\n==== File < {file} > ====")

    # email regex format
    emailRegex = re.compile(r'\w+@\w+\.\w{2,4}')
    email = emailRegex.findall(textStr)
    matchPrint(email, file, "email(s)")

    # telephone regex format
    telRegex = re.compile(r'\d{3}-\d{8}|\d{4}-\d{7}|\(\d{2,4}\)\d{6,7}|\(\d{2,4}\)[- ]?\d+[- ]\d+|\d[- ]?\d{3}[- ]?\d{3}[- ]?\d{4}')
    tel = telRegex.findall(textStr)
    matchPrint(tel, file, "telephone number(s)")

    # URL regex format
    urlRegex = re.compile(r"[https://|http://]*\w+\.\w+\.\w+")
    url = urlRegex.findall(textStr)
    matchPrint(url, file, "URL link(s)")

    # print('\n')
    fileText.close()