#! python3
# shop.py - Can purchase items from a shop keep inventory.

import os, shelve
from items import npcInv, itemCost, playerInv

# check to see what items the shop has and how many and how much
def checkItems():
    for item, amount in npcInv.items():
        try:
            print(str(amount) + ' x ' + item + ' - ' + str(itemCost[item]) + ' Gold each')
        except KeyError:
            continue

# ask to buy something
def shopKeep():
    while True:
        print('Would you like to buy something? (Y/N)')
        yesNo = input().upper()
        if yesNo == 'Y':
            print('These are the items we have in stock:')
            checkItems()
            break
        elif yesNo == 'N':\
            exit()
        else:
            continue

shopKeep()
# accept player prompt
print('What would you like to purchase? (# Item)\nYou have ' + str(playerInv['Gold']) + ' Gold.' )
# deduct item and cost
# show new inventory
# ask player if they want to buy anything else or exit