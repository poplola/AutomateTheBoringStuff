#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re
from pathlib import Path

# create american date files in folder below:
# /Users/flaviolago/Documents/Work/Training/Python/MSCode Projects/TestFile_L/10/renameDates


amerDates = ['01-23-1998', '12-24-2020','abc4-3-2008test']
p = Path(Path.cwd() / 'renameDates')
print(f'cwd path : {p}')

for i in range(len(amerDates)):
    # print('i : ', i)
    amerFiles = open(f'{amerDates[i]}.txt', 'w')
    for j in amerDates:
        amerFiles.write(j+'\n')
    amerFiles.close








# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?)                     # all text before the date
                        ((0|1)?\d)-                     # one or two digits for the month
                        ((0|1|2|3)?\d)-                 # one or two digits for the day
                        ((19|20)\d\d)                   # four digits for the year
                        (.*?)$                          # all text after the date
                        """, re.VERBOSE)

# TODO: Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # TODO: Skip files without a date.
    if mo == None:
        continue

    # TODO: Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)


    # TODO: Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # TODO: Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # TODO: Rename the files.
    print(f'\n\nRenaming "{amerFilename}" to "{euroFilename}"...\n\n')
    #shutil.move(amerFilename, euroFilename)   # uncomment after testing

