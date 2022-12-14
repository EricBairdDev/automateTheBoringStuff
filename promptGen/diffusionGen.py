import os
from promptLists import promptList

# init variables
weighting = 0
positivePrompt = ['']
negativePrompt = ['']

def printOut():
    print('Positive prompts: ' + ', '.join(positivePrompt))
    print('Negative prompts: ' + ', '.join(negativePrompt))

# Positive and negative prompt

# ADD/LOWER WEIGHTING
while True:
    print('Would you like to ADD/LOWER weighting on an item?')


# SAVE
while True:
    print('Would you like to SAVE current prompts?')
    print('SAVE AS?')
    print('Current name exists would you like to OVERWRITE?')
# LOAD
while True:
    print('LOAD from FAVOURITES or TEMPLATES?')

# VIEW


# TEMPLATE ADDONS
while True:
    print('ADD prompts from template?')

# FAVOURITES
while True:
    print('Would you like to LOAD from FAVOURITES?')