import os
import re

regexFile = open('regexResult.txt', 'w')
matches = []

#  regex search
searchRegex = re.compile(r'''(
.*new\syork|mexico\?
)''', re.IGNORECASE | re.VERBOSE)

# for .txt all files in folder, open and read
listDir = os.listdir()
for file in range(len(listDir)):
    # check only .txt files
    if listDir[file].endswith('.txt'):
        # open file and copy content to variable, then join.
        openFile = open(listDir[file])
        readFile = openFile.readlines()
        readFile = '\n'.join(readFile)
        #print(readFile)
        for match in searchRegex.findall(readFile):
            matches.append(match)
    else:
        continue

print('\n'.join(matches))

# TODO: Create seperate file for matches to save, even if this is a rather useless regex