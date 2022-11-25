import random
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.
 
Sincerely,
Bob''') # you can you triple quotes for multiline strings

print("Hello there!\nHow are you?\nI'm doing fine.") # '\' escape characters
#use double quotes to use ' within the sentence, otherwise use \' escape character or \" as needed

print(r'That is Carol\'s cat.') #type r to get raw strings, useful for regular expressions as they include '\'




feelingList = ['great',
               'fantastic',
               'pretty good',
               'not so bad',
               'decent',
               'sad',
               'hurt',
               'unhappy']

adList = ['handsome',
          'sexy',
          'totally deranged',
          'like you need to cope',
          ]

menu = {'feeling': feelingList, 'adjective': adList}

print('How are you?')
feeling = str(input())
if feeling.lower() in menu['feeling']: # lower() method converts string to lowercase, reverse true for upper()
    print('I feel ' + feeling.lower() + ' too. And you look ' + adList[random.randint(0, len(adList))] + ' today too!')
else:
    print('I hope the rest of your day is good.')

