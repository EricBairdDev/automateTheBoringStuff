#! python3
#  diffusionPromptGen.py - Adds weighting for stable difusion prompts and adds comma

import pyperclip

def userPrompt():
    while True:
        prompt = str(input())
        if prompt == '':
            break
        else:
            if pPrompt == True:
                positivePrompt.append((lBracket * weighting) + prompt + (rBracket * weighting))
            else:
                negativePrompt.append((lBracket * weighting) + prompt + (rBracket * weighting))

def addWeight():
    while True:
        print('Would you like to add any weighted words? (y/n)')
        add = str(input())
        if add == 'y':
            weighting += 1
            break
        elif add == 'n':
            break
        else:
            print('Please enter y or n:')
            continue

weighting = 0
positivePrompt = []
negativePrompt = []
pPrompt = True
lBracket = '('
rBracket = ')'
#ask user for neutral words
print('Insert neutral prompts, enter between each prompt, enter nothing for next weighting:')
userPrompt()
#ask user for 1 weighting and so on.
addWeight()


print('Enter prompt for ' + str(weighting) + ' weighting:')
userPrompt()
#ask user for negative prompt
print('Enter neutral negative prompt:')
pPrompt = False

#ask user for weighting
print('Negative prompt for weighting ' + str(weighting) + ':')
#spit out prompt to be copy and pasted to clipboard
# pyperclip.copy() COMMENT OUT LATER