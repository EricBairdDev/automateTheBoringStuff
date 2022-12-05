#! python3
# shop.py - Can purchase items from a shop keep inventory.

import os, shelve
from items import npcInv, itemCost      #get items





# check to see what items the shop has and how many and how much
for item, amount in npcInv.items():
    print(item + ' x ' + str(amount))
# ask to buy something
# accept player prompt
# deduct item and cost
# show new inventory
# ask player if they want to buy anything else or exit