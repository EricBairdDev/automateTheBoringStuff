myPets = ['Zoey', 'Sargent', 'Dutchess', 'Fat-Tailed']
print('Enter a pet name, enter nothing to quit:')

while True:
    name = str(input())
    if name not in myPets:
        print('I do not have a pet named ' + name)
        continue
    else:
        print(name + ' is my pet.')
        break