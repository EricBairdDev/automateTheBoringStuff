#! python3
# selectCopy.py - prompts for a specific file type and copies files to another folder

import os, shutil

# TODO: walk through folder tree

print(r'Input folder tree to copy. (Include "\\")')
#folder = str(input())
folder = 'C:\\Users\\ericm\\PycharmProjects\\ATBS\\Chap_9_Organizing_Files'


# TODO: prompt user what file type

print(r'What file type would you like to copy? Include "."')
fileType = str(input())


# TODO: search for file type

for folderName, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith(fileType):
            #test print
            print(folderName + '\\' + filename)
            # copy files
            try:
                shutil.copy(folderName + '\\' + filename, '/backupfiles')
            except shutil.SameFileError:
                print('Already backed')



