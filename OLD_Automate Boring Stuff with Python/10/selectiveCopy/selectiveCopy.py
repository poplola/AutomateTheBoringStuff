
# Python 3
# Write a program that walks through a folder tree and searches 
# for files with a certain file extension (such as .pdf or .jpg).
# Copy these files from whatever location they are in to a new folder.

import shutil, os
from pathlib import Path

def selectiveCopy(sFolder, dFolder):
    fileEx = '.txt'
    # copyFileList = []
    numFile = 0
    for foldername, subfolders, filenames in os.walk(sFolder):
        # print('\nfoldername : ', foldername)
        # print('\nsbfolders : ', subfolders)
        # print('\nfilenames : ', filenames)
        for filename in filenames:
            if fileEx in filename:
                dest = shutil.copy(f'{foldername}/{filename}', dFolder)
                # dest = shutil.copy(foldername / filename, dFolder)
                # print(f'====fileEx : ===={filename}\n')
                # print(f'++++folder name : ++++{foldername}\n\n')
                # print(f'{foldername}/{filename}')
                # print('dfoldr : ????', dFolder)

                # copyFileList.append(filename)

                numFile += 1
                # print(numFile)
                print(f'File #{numFile} : {filename} \n\t(File Folder: {foldername})\n')


    print(f'\n==== There are {numFile} {fileEx} file(s) copied into a new folder ==== \n{dFolder}\n\n')
    # print(copyFileList)

    # for i in range(len(copyFileList)):
    #     print(f' {i+1} : {copyFileList[i]}')
    # print('===========================\n')




def main():
    sPath = '/Users/flaviolago/Documents/Work/Training/Python/MSCode Projects/TestFile_L/10'
    dPath = '/Users/flaviolago/Documents/Work/Training/Python/MSCode Projects/TestFile_L/test'
    
    selectiveCopy(sPath, dPath)


if __name__ == "__main__": main()