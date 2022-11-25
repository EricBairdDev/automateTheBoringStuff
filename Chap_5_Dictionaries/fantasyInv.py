def displayInventory():
    for k, v in inventory.items(): #for each keyvalue pair, print string of value + key
        print(str(v) + ' ' + k)

def itemTotal():
    itemTotal = 0
    for v in inventory.values(): #iterate through each value and add each to itself
        itemTotal += v
    print('Total number of items: ' + str(itemTotal))

def addToInventory(inventory, theLoot):
    for i in range(len(theLoot)):
        if theLoot[i] in inventory:  # if 'word' is in inv
            inventory[theLoot[i]] += 1  # add one to the current total
        else:
            inventory.setdefault(theLoot[i], 1)  # if loot is not in dict,
                                                 # add it and set it to 1



inventory = {'rope': 1,
             'torch': 6,
             'gold coin': 42,
             'dagger': 1,
             'arrow': 12}

dragonLoot = ['gold coin',
              'dagger',
              'gold coin',
              'gold coin',
              'Holy Grail',
              'ruby']

minionLoot = ['gold coin',
              'tiny dagger',
              'gold coin']


addToInventory(inventory, dragonLoot)
addToInventory(inventory, minionLoot) # confirming thing will do what I expect. It does.
# Join dragon + minion loot up the second last + and the last loot.
print('You have gained: ' + ', '.join(dragonLoot + minionLoot[:-1]) + ', and ' + minionLoot[-1])
print('Inventory:')
displayInventory()
itemTotal()