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

def posNeg():
    while True:
        print('Positive or negative? (p/n)')
        posNeg = str(input())
        if posNeg == 'p':
            pPrompt = True
            break
        elif posNeg == 'n':
            pPrompt = False
            break
        else:
            continue

def options():
    print('Would you like to ADD, REMOVE, VIEW, or COPY anything to/from the lists? EXIT to exit.')
    while True:
        option = str(input())
        if option == 'ADD':
            posNeg()
            print('What would you like to add?')
            userPrompt()
            options()
        elif option == 'REMOVE':
            posNeg()
            print('Input number of item to be removed:')
            num = 0
            num = input()
            if num.isdigit():
                global pPrompt
                if pPrompt == True:
                    print(positivePrompt[num] + ' has been removed.')
                    positivePrompt.remove(positivePrompt[num])
                    options()
                else:
                    print(negativePrompt[num] + ' has been removed.')
                    negativePrompt.remove(negativePrompt[num])
                    options()
            else:
                print('Please enter a number')
                continue
        elif option == 'VIEW':
            printOut()
            options()
        elif option == 'COPY':
            posNeg()
            if pPrompt == True:
                pyperclip.copy(', '.join(positivePrompt))
                print('Copied: ' + ', '.join(positivePrompt))
            else:
                pyperclip.copy(', '.join(negativePrompt))
                print('Copied: ' + ', '.join(negativePrompt))
        elif option == 'EXIT':
            exit()
        else:
            continue

def printOut():
    print('Positive prompts: ' + ', '.join(positivePrompt))
    print('Negative prompts: ' + ', '.join(negativePrompt))

weighting = 0
positivePrompt = []
negativePrompt = []
pPrompt = True  #Varible to toggle between positive and negative prompt

#ask user for positive prompts
print('Insert neutral prompts, enter between each prompt, enter nothing for next weighting:')
userPrompt()

#ask user for negative prompts
print('Enter neutral negative prompts:')
pPrompt = False
weighting = 0
userPrompt()

#spit out prompt to be copy and pasted to clipboard
# pyperclip.copy() COMMENT OUT LATER
printOut()

#ask for options
options()