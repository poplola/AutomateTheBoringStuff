# Python 3
# finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, 
# in a single folder and locates any gaps in the numbering 
# (such as if there is a spam001.txt and spam003.txt but no spam002.txt). 
# Have the program rename all the later files to close this gap.

import os, glob, re
from pathlib import Path

preStr = 'spam_'
p = Path ('/Users/flaviolago/Documents/Work/Training/Python/MSCode Projects/TestFile_L/test/test_1')


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
    # pathFold = Path.cwd() / test / test_1 
    zList = list(p.glob(preStr+'*.*'))
    zList.sort()
    # print(zList)
    # fileList = os.listdir(p)
    # fileList.sort()
    # print('file list : \n', fileList)

    print ("="*80)
    fileNum = 1
    renameCount = 0
    for i in zList:
        # print(i.stem)
        # print(i)
        fileStem = i.stem
        numStr = ''
        
        # print(f'ext : {filename}\n{ext}') 
        for j in range(len(preStr),len(fileStem)):
            numStr += fileStem[j]
        # print(f'numStr : {numStr}')

    #     numRegex = re.compile(r'\d\d\d')
    #     mo = numRegex.findall(i)
    #     print(f'mo {i} : ', mo)
        
    #   =====================================  
        if int(numStr) == fileNum:
            fileNum +=1
            continue
        else:
            # n = fileNum + 1
            # print('n : ', n)
            # print('len of fileList : ', len(fileList))
            for j in range(fileNum-1, len(zList)):
                # mo_1 += 1
                oldName = os.path.basename(zList[j])
                ext = os.path.splitext(i)[1]          
                os.rename(f'{zList[j]}', f"{p}/{preStr}{str(fileNum).rjust(3,'0')}{ext}")
                # Path('my/library.tar.gz').suffix
                # f"{p}/{preStr}{str(i+1).rjust(3,'0')}.txt"
                # print(f'souce file : {p}/{fileList[j]}')
                # print(f'souce file : {p/str(fileList[j]}')
                # print(f"destination file : {p/f'{preStr}{str(mo_1+1)}.txt'}")
                print(f"Renaming file [{oldName}] to [{preStr}{str(fileNum).rjust(3,'0')}{Path(i).suffix}]")
                fileNum += 1
                renameCount += 1
            break
    print(f'\n======= There are {renameCount}/{str(len(zList))} file(s) renamed =======\n')
    # ====================================


def main():
    # createFiles()
    fillFileGaps()


if __name__ == "__main__": main()