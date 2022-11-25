print('What is your age?') #ask for age
myAge = input() #stores input into variable myAge
print('You will be ' + str(int(myAge) + 1) + ' in a year')

#print('You will be ' + str(int(myAge) + 1) + ' in a year')
# print('You will be ' + str(int('4') + 1) + ' in a year')
# print('You will be ' + str(4 + 1) + ' in a year')
# print('You will be ' + str(5) + ' in a year')
# print('You will be ' + str(5) + ' in a year')
# print('You will be ' + '5' + ' in a year')
# print('You will be 5 in a year')


# Q: 1. Which of the following are operators, and which are values?
# *        O
# 'hello'  value
# -88.8    value
# -        O
# /        O
# +        0
# 5        value

# Q: 2. Which of the following is a variable, and which is a string?
# spam variable
# 'spam' string

# Q: 3. Name three data types.
# Integers
# Floating point
# Numbers
# Strings


# Q: 4. What is an expression made up of? What do all expressions do?
# An expression is a combination of values and operators. All expressions evaluate (that is, reduce) to a single value.


# Q: 5. This chapter introduced assignment statements, like spam = 10. What is the
# difference between an expression and a statement?
# An expression evaluates to a single value. A statement does not.

# Q: 6. What does the variable bacon contain after the following code runs?
# bacon = 20
# bacon + 1
# The bacon variable is set to 20. The bacon + 1 expression does not reassign the value in bacon
# (that would need an assignment statement: bacon = bacon + 1).


# Q: 7. What should the following two expressions evaluate to?
# 'spam' + 'spamspam'
# 'spam' * 3
# spamspamspam

# Q: 8. Why is eggs a valid variable name while 100 is invalid?
# Variables can't begin with numbers


# Q: 9. What three functions can be used to get the integer, floating-point number,
# or string version of a value?
# int()
# float()
# str()


# Q: 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten ' + 99 + ' burritos.'
# Extra credit: Search online for the Python documentation for the len()
# function. It will be on a web page titled “Built-in Functions.” Skim the list of
# other functions Python has, look up what the

# The expression causes an error because 99 is an integer, and only strings can be concatenated to other
# strings with the + operator. The correct way is
# 'I have eaten ' + str(99) + ' burritos.'