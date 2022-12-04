#! python3
# selectCopy.py - prompts for a specific file type and copies files to
# C:\\Users\\ericm\\PycharmProjects\\ATBS\\backupfiles

import os, shutil

# search for file type
def searchFolder(folder):
    for folderName, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(fileType):
                #test print
                print(folderName + '\\' + filename + ' --copied')
                # copy files
                try:
                    shutil.copy(folderName + '\\' + filename, 'C:\\Users\\ericm\\PycharmProjects\\ATBS\\backupfiles\\' + 'backup_' + filename)
                except shutil.SameFileError:
                    continue


    # walk through folder tree
    print(r'Input folder tree to copy. (Include "\\")')
    # TODO: Allow for input
    #folder = str(input()) #uncomment to allow input
    # TODO: Check if directory exists or not
    folder = 'C:\\Users\\ericm\\PycharmProjects\\ATBS\\Chap_9_Organizing_Files'

    # prompt user what file type
    print(r'What file type would you like to copy? Include "."')
    fileType = str(input())
    break

# TODO: Add ability to copy another folder/filetype, create function

searchFolder(folder)

