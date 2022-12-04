#! python3
# gapFill.py - given a sequence of file names, if those file names are out of order
# (ie. spam001.txt, spam003.txt) the files are renamed to the appropriate number

import os, shutil

fileType = []
folderName = 'C:\\Users\\ericm\\PycharmProjects\\ATBS\\Chap_9_Organizing_Files\\gap_fill\\'
print('Enter new file prefix')
prefix = str(input())

#check file in folder
folder = os.listdir(folderName)

for files in range(len(folder)):
    #temp print
    print(folder[files])
    fileStr = str(folder[files])

    # check names of files
    #shutil.move(folderName + [files])
    print(folderName + folder[files])
    print(folderName + prefix + str(files))
    # copy and rename file in correct order
#delete old file

if folder[0][files] == '.':
    fileType.append(folder[0][fileType])