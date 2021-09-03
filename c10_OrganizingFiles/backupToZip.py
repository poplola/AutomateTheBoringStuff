#! Python3
# BACKING UP A FOLDER INTO A ZIP FILE
# backupToZip.py
"""
Add folder to zip folder

Say you’re working on a project whose files you keep in a folder named C:\AlsPythonBook. You’re worried about losing your work, so you’d like to create ZIP file “snapshots” of the entire folder. You’d like to keep different versions, so you want the ZIP file’s filename to increment each time it is made; for example, AlsPythonBook_1.zip, AlsPythonBook_2.zip, AlsPythonBook_3.zip, and so on. You could do this by hand, but it is rather annoying, and you might accidentally misnumber the ZIP files’ names. It would be much simpler to run a program that does this boring task for you.

Ideas for Similar Programs
You can walk a directory tree and add files to compressed ZIP archives in several other programs. For example, you can write programs that do the following:
Walk a directory tree and archive just files with certain extensions, such as .txt or .py, and nothing else.
Walk a directory tree and archive every file except the .txt and .py ones.
Find the folder in a directory tree that has the greatest number of files or the folder that uses the most disk space.
"""

import zipfile
import os
from time import ctime
from pathlib import Path


class ZipUtilities:

    def toZip(self, file, filename):
        zip_file = zipfile.ZipFile(filename, 'w')
        if os.path.isfile(file):
            zip_file.write(file)
        else:
            self.addFolderToZip(zip_file, file)
        zip_file.close()

    def addFolderToZip(self, zip_file, folder): 
        for file in os.listdir(folder):
            full_path = os.path.join(folder, file)
            if os.path.isfile(full_path):
                print('File added: ' + str(full_path))
                zip_file.write(full_path)
            elif os.path.isdir(full_path):
                print('Entering folder: ' + str(full_path))
                self.addFolderToZip(zip_file, full_path)

def main():
    utilities = ZipUtilities()
    filename = f'BackupFile_{ctime()}.zip'
    # os.chdir(f'{str(Path.cwd())}/c10_OrganizingFiles/backupToZip/')
    # directory = f'{str(Path.cwd())}/c10_OrganizingFiles/backupToZip'
    directory = f'{str(Path.cwd())}/c10_OrganizingFiles/'    
    utilities.toZip(directory, filename)

main()