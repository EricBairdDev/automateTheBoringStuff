#! python3
#  diffusionPromptGen.py - Adds weighting for stable difusion prompts and adds comma

import pyperclip

#ask user for neutral words
print('Insert neutral prompts, enter between each prompt, enter nothing for next weighting:')
#ask user for 1 weighting and so on.
weighting = 0
print('Enter prompt for ' + str(weighting) + ' weighting:')
#ask user for negative prompt
print('Enter neutral negative prompt:')
#ask user for weighting
print('Negative prompt for weighting ' + str(weighting) + ':')
#spit out prompt to be copy and pasted to clipboard
# pyperclip.copy() COMMENT OUT LATER