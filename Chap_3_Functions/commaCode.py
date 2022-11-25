def returnList(theList):
    #iterate over list of items
    newString = ''
    for i in range(len(theList) - 1): # do this the length of the list minus 1
        newString = newString + (theList[i] + ', ') # add word and comma to total string
    return newString



def askUser(): #function to input another item
    print('What would you like to add to the list? Please press enter after each item, enter nothing to see full list.')
    while True:
        item = str(input())
        if item in theList: #what to do if item is already in the list
            print('You\'ve already added ' + item + ' to the list, please enter another item:')
            continue
        elif item == '': # enter nothing to see list
            print('You currently have: ' + returnList(theList) + 'and ' + theList[-1] + '.')
            break
        else: # otherwise must be added to the list
            theList.append(item)
            continue



theList = ['apples', 'pears', 'onions', '42'] #give it something if no items entered by user

askUser() # call function to ask for user input


while True:
    moreItems = input('Would you like to add more? (Y/N) \n').upper() #ask user if they'd like to add more, converts to upper case so y/Y/n/N are all accepted.
    if moreItems == 'N': # quits
        break
    elif moreItems == 'Y': # calls function to ask for user input
        askUser()
    else: # user enters something other than y/n
        print('Please answer Y or N.')
        continue



