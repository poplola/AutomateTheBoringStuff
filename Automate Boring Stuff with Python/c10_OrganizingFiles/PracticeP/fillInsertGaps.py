#! Python3
# Filling/Insert in the filename Gaps
# fillInsertGaps.py
"""
Challenge 1:
    Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, 
    in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt). 
    Have the program rename all the later files to close this gap.

Challenge 2:
    As an added challenge, write another program that can insert gaps into numbered files so that a new file can be added.
"""

import os, shutil
from pathlib import Path

srcDir = Path.cwd() / "c10_OrganizingFiles/PracticeP/fillingGaps/"
fileNum = 10
prefixWord = 'spam'

def insertGaps(directory):

    # Create file folder "fillingGaps"
    if not directory.exists():
        os.mkdir(directory)

    # Create prefix word "spam" gap files in the fillingGaps folder
    gapStartNum = 20
    gapNum = 4
    for i in range(fileNum):
        fileObj = open(directory/f"{prefixWord}{str(i+gapStartNum).rjust(3,'0')}.txt", 'w')
        fileObj.write(f"{directory}/"+f"{prefixWord}{str(i+gapStartNum).rjust(3,'0')}.txt")
        gapStartNum += gapNum

def fillGaps(directory):
    # rename the file gaps.
    for filefolder, subfolders, filenames in os.walk(directory):   
        filenames.sort()
        preFileList = []
        for filename in filenames:
            if prefixWord in filename:
                preFileList.append(filename)
        startNum = int(preFileList[0].split('.')[0][len(prefixWord):])
        # print(startNum)

        for filename in preFileList:
            # print(filename)
            # print(filename.split('.')[0])
            fileExtension = filename.split('.')[1]
            newname = prefixWord + f"{str(startNum).rjust(3,'0')}" + '.' + fileExtension
            if filename != newname:
                print(f"Renaming file <{filename}> ===> <{newname}>")
                os.rename(f"{filefolder}/{filename}", f"{filefolder}/{newname}")
            startNum += 1
    print('\n', f" {len(preFileList)-1} files have been renamed ".center(100, '='), '\n')

def deleteGaps(directory):
    for filefolder, subfolders, filenames in os.walk(directory):   
        for filename in filenames:
            if prefixWord in filename:
                os.unlink(f"{filefolder}/{filename}")
                print(f"Deleting file <{filename}> ... DONE!")
        print('\n', f" {len(filenames)} files have been deleted ".center(100, '='), '\n')

def main():
    # Choose one function to run
    insertGaps(srcDir)
    # fillGaps(srcDir)
    # deleteGaps(srcDir)

if __name__ == '__main__': 
    main()