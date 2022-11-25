import os
import re

regexFile = open('regexResult.txt', 'w')
matches = []

searchRegex = re.compile(r'''(
.*new\syork|mexico\?
)''', re.IGNORECASE | re.VERBOSE)

# TODO: for .txt all files in folder, open and read

listDir = os.listdir()
for file in range(len(listDir)):
    if listDir[file].endswith('.txt'):
        print(listDir[file])
        openFile = open(listDir[file])
        readFile = openFile.readlines()
        for reg in searchRegex.findall(readFile):
            matches.append(reg)
        print(readFile)
    else:
        continue

print(matches)

# TODO: regex search

# TODO: