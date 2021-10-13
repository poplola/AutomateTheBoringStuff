# Python3
# walks through a folder tree and searches for exceptionally large files or folders—say, 
# ones that have a file size of more than 100MB. (Remember that to get a file’s size, 
# you can use os.path.getsize() from the os module.) 
# Print these files with their absolute path to the screen.


import os, pyinputplus as pyip
from pathlib import Path



def deletingUnneededFiles(dPath):
    print('\n\n')
    numFile = 0

    # show all files and file size under the folder
    for foldername, subfolders, filenames in os.walk(dPath):
        for filename in filenames:
            fileSize = os.path.getsize(f'{foldername}/{filename}')
            print(f"{filename.rjust(30)} : {fileSize} {'bytes'.rjust(10)}")
            numFile += 1
    print(f'\n====== There are {numFile} file(s) found =======\n')

    # input the size of file to delete
    deleSize = int(pyip.inputInt('\nPlease enter the minumium size number of file that you want to delete : '))
    print('\n')
    numDeleteFile = 0
    
    # DELETE the files that the file size is greater than input number
    for foldername, subfolders, filenames in os.walk(dPath):
        for filename in filenames:
            fileSize = os.path.getsize(f'{foldername}/{filename}')
            if fileSize >= deleSize:
                print(f"deleting file {numDeleteFile + 1} ... \n\t{filename} : {fileSize} {'bytes'.rjust(10)}")
                print(f'\tfile path : {foldername}\n')
                os.unlink(f'{foldername}/{filename}')
                numDeleteFile += 1
    print(f'\n====== There are {numDeleteFile} file(s) deleted =======\n')

    numFile = 0
    # show all files and file size under the folder again after deleting files
    for foldername, subfolders, filenames in os.walk(dPath):
        for filename in filenames:
            fileSize = os.path.getsize(f'{foldername}/{filename}')
            print(f"{filename.rjust(30)} : {fileSize} {'bytes'.rjust(10)}")
            numFile += 1
    print(f'\n====== There are {numFile} file(s) found =======\n')




def main():
    dFolderPath = '/Users/flaviolago/Documents/Work/Training/Python/MSCode Projects/TestFile_L/test'

    deletingUnneededFiles(dFolderPath)


if __name__ == "__main__": main()
