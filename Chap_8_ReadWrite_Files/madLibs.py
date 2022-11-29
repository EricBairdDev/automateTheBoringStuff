#! python3
# madLibs.py - program that reads in text files and lets the user
# add their own text anywhere the word ADJECTIVE, NOUN, ADVERB,
# or VERB appears in the text file

import os
import re

# Create/Open files for input/output
madLibFile = open('madlibs.txt')
madLibAnswer = open('madanswer.txt', 'w')

madContent = madLibFile.read()
madContent = madContent.split()

# Ask user for verb/adjective/noun/adverb
for word in range(len(madContent)):
    # check each word for type of word
    if madContent[word].startswith('VERB') or madContent[word].startswith('ADJECTIVE') or \
            madContent[word].startswith('ADVERB') or madContent[word].startswith('NOUN'):
        # check if word ends with punctuation and remove the punctuation
        if madContent[word].endswith(',') or madContent[word].endswith('.') or madContent[word].endswith(';') or \
                madContent[word].endswith(':') or madContent[word].endswith('!') or madContent[word].endswith('\'') or \
                madContent[word].endswith('"'):
            print('Please enter a ' + madContent[word][:-1].lower() + ':')
        else:
            print('Please enter a ' + madContent[word].lower() + ':')
        answer = str(input())
        # if punctuation exists add it to the end of the new word
        if madContent[word].endswith(',') or madContent[word].endswith('.') or madContent[word].endswith(';') or \
                madContent[word].endswith(':') or madContent[word].endswith('!') or madContent[word].endswith('\'') or \
                madContent[word].endswith('"'):
            answer = answer + madContent[word][-1]
            madContent.remove(madContent[word])
            madContent.insert(word, answer)
        else:
            madContent.remove(madContent[word])
            madContent.insert(word, answer)
    else:
        continue

# Print results to screen and save to txt
madContent = ' '.join(madContent)
print(madContent)
madLibAnswer.write(madContent)

# Close files
madLibFile.close()
madLibAnswer.close()

# TODO: See if there's a way to shorten if statements for punctuation