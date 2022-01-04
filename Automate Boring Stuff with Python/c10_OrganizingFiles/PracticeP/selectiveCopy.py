#! Python3
# Selective Copy
# selectiveCopy.py
"""
Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). 
Copy these files from whatever location they are in to a new folder.
"""

import shutil, os
from pathlib import Path

copyDir = Path.cwd() / "c10_OrganizingFiles/PracticeP/selectiveCopy/copyDir"
newDir = Path.cwd() / "c10_OrganizingFiles/PracticeP/selectiveCopy/newDir"
fileExtdic = {'.pdf': 0, '.jpg': 0, '.txt': 0}

if not newDir.exists():
    os.mkdir(newDir)

# walk through whole folder tree
for folderName, subFolders, fileNames in os.walk(copyDir):
    print(f"\n==== {folderName} ====")

    # print subfolder list in folder
    for subFolder in subFolders:
        print(f'+++ {subFolder} ++++')

    # print file name in folder
    for fileName in fileNames:
        print(f" ---- {fileName} -----")
        fileExtension = Path(fileName).suffix
        if fileExtension in fileExtdic.keys():
            shutil.copy(f"{folderName}/{fileName}", newDir)
            fileExtdic[fileExtension] += 1

for fileExt in fileExtdic.keys():
    print(f"\n\t{fileExtdic[fileExt]} <{fileExt}> file(s) found and copied to new folder.")

#  sum all values in dictionary
totalCopiedFiles = sum(fileExtdic.values())
print("\n"+f" Totally, {totalCopiedFiles} file(s) found and copied to new folder! ".center(70, '=')+'\n')