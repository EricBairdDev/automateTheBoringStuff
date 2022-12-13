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
                positivePrompt.append(prompt)
            else:
                negativePrompt.append(prompt)


weighting = 0
positivePrompt = []
negativePrompt = []
pPrompt = True
#ask user for neutral words
print('Insert neutral prompts, enter between each prompt, enter nothing for next weighting:')
userPrompt()
#ask user for 1 weighting and so on.
print('Enter prompt for ' + str(weighting) + ' weighting:')
userPrompt()
#ask user for negative prompt
print('Enter neutral negative prompt:')
pPrompt = False

#ask user for weighting
print('Negative prompt for weighting ' + str(weighting) + ':')
#spit out prompt to be copy and pasted to clipboard
# pyperclip.copy() COMMENT OUT LATER