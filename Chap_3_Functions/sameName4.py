def spam():
    print(eggs) #ERROR
    eggs = 'spam local' # Variable declared BEFORE fixes error, python sees that the variable is declared, but so won't
    #wont use global, but you also need to declare first.

eggs = 'global'
spam()