#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.
"""
Say your boss emails you thousands of files with American-style dates (MM-DD-YYYY) in their names and needs them renamed to European-style dates (DD-MM-YYYY). This boring task could take all day to do by hand! Let’s write a program to do it instead.

Here’s what the program does:
1. It searches all the filenames in the current working directory for American-style dates.
2. When one is found, it renames the file with the month and day swapped to make it European-style.

This means the code will need to do the following:
1. Create a regex that can identify the text pattern of American-style dates.  
2. Call os.listdir() to find all the files in the working directory.
3. Loop over each filename, using the regex to check whether it has a date. 4. If it has a date, rename the file with shutil.move().
"""

import shutil, os, re, random
from pathlib import Path

# Create a regex that matches files with the American date format. 
datePattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-         # one or two digits for the month
    ((0|1|2|3)?\d)-     # one or two digits for the day
    ((19|20)\d\d)       # four digits for the year
    (.*?)$              # all text after the date
    """, re.VERBOSE)

workingFolder = './c10_OrganizingFiles/renameDates'
# workingFolderTest = './c10_OrganizingFiles/renameDates/test'

# create date format '.txt' files
if not Path(workingFolder).is_dir():
    Path(workingFolder).mkdir()

# if not Path(workingFolderTest).is_dir():
#     Path(workingFolderTest).mkdir()

for i in range(10):
    dd = str(random.randint(0,2)) + str(random.randint(1,9))
    mm = '0' + str(random.randint(1,9))
    yyyy = str(random.randint(1900, 2099))
    fileName = mm + '-' + dd + '-' + yyyy
    # print(f"#{i+1} : {mm}-{dd}-{yyyy}")
    file = open(f'{workingFolder}/{fileName}.txt', 'w')
    file.write(f'{workingFolder}/{fileName}.txt')
    file.close()

# TODO: Loop over the files in the working directory. 
for amerFilename in os.listdir(workingFolder):

    print(amerFilename)
    mo = datePattern.search(amerFilename)

    # TODO: Skip files without a date.
    if mo == None:
        continue
    
    print(mo)
    # TODO: Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6) 
    afterPart = mo.group(8)

    # TODO: Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    print("beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart")
    print(f"{beforePart} + {dayPart} + '-' + {monthPart} + '-' + {yearPart} + {afterPart}")
    print("euroFilename = ", euroFilename)

    # TODO: Get the full, absolute file paths.
    # absWorkingDir = os.path.abspath(workingFolder/f'{amerFilename}')
    # amerFilename = os.path.join(absWorkingDir, amerFilename) 
    # euroFilename = os.path.join(absWorkingDir, euroFilename)
    # os.path.join(absWorkingDir, euroFilename)
    print(f'{workingFolder}/{amerFilename}', f'{workingFolder}/{euroFilename}\n\n')
    shutil.copy2(f'{workingFolder}/{amerFilename}', f'{workingFolder}/{euroFilename}')

    # TODO: Rename the files.
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    # shutil.move(amerFilename, euroFilename) # uncomment after testing