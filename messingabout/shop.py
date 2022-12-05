#! python3
# shop.py - Can purchase items from a shop keep inventory.

import os, shelve
from items import npcInv, itemCost

# check to see what items the shop has and how many and how much
def checkItems():
    for item, amount in npcInv.items():
        print(item + ' x ' + str(amount))

# ask to buy something
def shopKeep():
    while True:
        print('Would you like to buy something? (Y/N)')
        yesNo = input().upper()
        if yesNo == 'Y':
            print('These are the items we have in stock:')
            checkItems()
        elif yesNo == 'N':\
            exit()
        else:
            continue

shopKeep()
# accept player prompt
# deduct item and cost
# show new inventory
# ask player if they want to buy anything else or exit