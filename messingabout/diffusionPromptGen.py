#! python3
#  diffusionPromptGen.py - Adds weighting for stable difusion prompts and adds comma

import pyperclip

weighting = 0
positivePrompt = []
negativePrompt = []

#ask user for neutral words

while True:
    print('Insert neutral prompts, enter between each prompt, enter nothing for next weighting:')
    prompt = str(input())
    if prompt == '':
        break
    else:
        positivePrompt.append(prompt)

#ask user for 1 weighting and so on.
while True:
    print('Enter prompt for ' + str(weighting) + ' weighting:')
    prompt = str(input())
#ask user for negative prompt
print('Enter neutral negative prompt:')
#ask user for weighting
print('Negative prompt for weighting ' + str(weighting) + ':')
#spit out prompt to be copy and pasted to clipboard
# pyperclip.copy() COMMENT OUT LATER