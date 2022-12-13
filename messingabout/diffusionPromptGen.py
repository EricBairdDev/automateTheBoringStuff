#! python3
#  diffusionPromptGen.py - Adds weighting for stable diffusion prompts and adds comma

import pyperclip

def userPrompt():
    while True:
        prompt = str(input())
        # if nothing entered ask if weight is wanted.
        if prompt == '':
            addWeight()
            break
        else:
            #if positie prompt add to positive list, if not negative list
            if pPrompt == True:
                positivePrompt.append(('(' * weighting) + prompt + (')' * weighting))
            else:
                negativePrompt.append(('(' * weighting) + prompt + (')' * weighting))

def addWeight():
    while True:
        print('Would you like to add any weighted words? (y/n)')
        add = str(input())
        #ask for added weight then prompt for word
        if add == 'y':
            global weighting
            weighting += 1
            print('Prompt for weighting ' + str(weighting) + ':')
            userPrompt()
            break
        elif add == 'n':
            break
        else:
            print('Please enter y or n:')
            continue

weighting = 0
positivePrompt = []
negativePrompt = []
pPrompt = True  #Varible to toggle between positive and negative prompt

#ask user for positive prompts
print('Insert neutral prompts, enter between each prompt, enter nothing for next weighting:')
userPrompt()

#ask user for negative prompts
print('Enter neutral negative prompt:')
pPrompt = False
weighting = 0
userPrompt()

#spit out prompt to be copy and pasted to clipboard
# pyperclip.copy() COMMENT OUT LATER
positivePrompt = ', '.join(positivePrompt)
print(positivePrompt)
negativePrompt = ', '.join(negativePrompt)
print(negativePrompt)