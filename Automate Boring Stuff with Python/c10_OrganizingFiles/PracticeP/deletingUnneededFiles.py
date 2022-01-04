#! Python3
# Deleting Unneeded Files
# deletingUnneededFiles.py
"""
Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, ones that have a file size of more than 100MB. 
(Remember that to get a file’s size, you can use os.path.getsize() from the os module.) 
Print these files with their absolute path to the screen.
"""

import os, shutil
from pathlib import Path

delFileDir = Path.cwd() / "c10_OrganizingFiles/PracticeP/deletingUnneededFiles/toBeDeleted"
backupDir = Path.cwd() / "c10_OrganizingFiles/PracticeP/deletingUnneededFiles/backup"

fileSizeToDelete = 100

# copy whole backup folder tree to toBeDeleted folder
if not delFileDir.exists():
    shutil.copytree(backupDir, delFileDir)

# walk through the folder and get file size
for filefolder, subfolders, filenames in os.walk(delFileDir):
    print(f"\nCurrent folder is : \n{filefolder}")
    print(f"\n\t{' FILE NAME'.rjust(40, '=')} : {'FILE SZIE '.ljust(40, '=')}")        
    for filename in filenames:
        fileSize = os.path.getsize(f"{filefolder}/{filename}")
        delStr = ''
        if fileSize >=fileSizeToDelete:
            delStr = f'(DELETED OVER {fileSizeToDelete})'
            os.unlink(f"{filefolder}/{filename}")
        print(f"\t{filename.rjust(40)} : {str(fileSize).ljust(10)} byte(s)"+ delStr)


print("\n\t" + f" File(s) under size {fileSizeToDelete} byte(s)".center(80, '='))        
for filefolder, subfolders, filenames in os.walk(delFileDir):

     for filename in filenames:
        fileSize = os.path.getsize(f"{filefolder}/{filename}")
        print(f"\t{filename.rjust(40)} : {str(fileSize).ljust(10)} byte(s)")


