#! python3
# gapFill.py - given a sequence of file names, if those file names are out of order
# (ie. spam001.txt, spam003.txt) the files are renamed to the appropriate number

import os, shutil

folderName = 'C:\\Users\\ericm\\PycharmProjects\\ATBS\\Chap_9_Organizing_Files\\gap_fill'

#check file in folder
folder = os.listdir(folderName)

for files in range(len(folder)):
    #temp print
    print(files)
    print(folder[files])

    # check names of files

    # copy and rename file in correct order
#delete old file

