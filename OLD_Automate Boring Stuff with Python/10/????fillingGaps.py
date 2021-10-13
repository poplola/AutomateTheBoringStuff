#! Python 3
# finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, 
# in a single folder and locates any gaps in the numbering 
# (such as if there is a spam001.txt and spam003.txt but no spam002.txt). 
# Have the program rename all the later files to close this gap.
# Error when delete the 1st fille


import os, glob, re
from pathlib import Path

preStr = 'spam_'
p = '/Users/flaviolago/Documents/Work/Training/Python/MSCode Projects/TestFile_L/test/test_1'

# create files for testing
def createFiles():

    for i in range(10):
        filePrefix = open(f"{p}/{preStr}{str(i+1).rjust(3,'0')}.txt", 'w')
        # filePrefix = open(f'{P}/{preStr}{str(i+1)')
        # print(filePrefix)
      
        filePrefix.write(f"{preStr}{str(i+1).rjust(3,'0')}.txt\n")
        print(f"Creating File #{i+1} : {preStr}{str(i+1).rjust(3,'0')}.txt")
        filePrefix.write(f'File Path: {p}')
        filePrefix.close()
    print(f'\n======= There are {str(i+1)} file(s) created =======\n')


def fillFileGaps():
    # pathFolder = Path(p)
    fileList = os.listdir(p)
    fileList.sort()
    print('file list : \n', fileList)

    print ("="*80+'\n')
    # indexNum = 0
    numRegex = re.compile(r'\d\d\d')
    renameCount = 0
    for i in range(len(fileList)):
        # print(i)
        mo = numRegex.findall(fileList[i])
        mo_1 = int(mo[0])
        mo = numRegex.findall(fileList[i+1])
        mo_2 = int(mo[0])
        # print(f'mo {fileList[i]} : ', mo)
        fileNumOrder = mo_2 - mo_1
        # indexNum += 1
        if fileNumOrder == 1:
            continue
        else:
            n = i + 1
            # print('n : ', n)
            # print('len of fileList : ', len(fileList))
            for j in range(n, len(fileList)):
                mo_1 += 1
                oldName = fileList[j]            
                os.rename(f'{p}/{fileList[j]}', f"{p}/{preStr}{str(mo_1).rjust(3,'0')}.txt")
                # f"{p}/{preStr}{str(i+1).rjust(3,'0')}.txt"
                # print(f'souce file : {p}/{fileList[j]}')
                # print(f'souce file : {p/str(fileList[j]}')
                # print(f"destination file : {p/f'{preStr}{str(mo_1+1)}.txt'}")
                print(f"Renaming file [{oldName}] to [{preStr}{str(mo_1).rjust(3,'0')}.txt]")
                renameCount += 1
            break
    print(f'\n======= There are {renameCount}/{str(len(fileList))} file(s) renamed =======\n')



def main():
    # createFiles()
    fillFileGaps()


if __name__ == "__main__": main()