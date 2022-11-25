while True:
    print("Enter your age:")
    age = input()
    if age.isdecimal():
        break
    print("Please enter a number for your age.")

while True:
    print("Select a new password (letters and numbers only):")
    password = input()
    if password.isalnum():
        break
    print("Passwords can only contain letters and numbers")

# isX string methods:
# isdecimal(), isalnum(), isalpha(), isspace(), istitle()

# The startswith() and endswith() String Methods
# The startswith() and endswith() methods return True if the string
# value they are called on begins or ends (respectively) with the string
# passed to the method; otherwise, they return False. Enter the
# following into the interactive shell:
# >>> 'Hello world!'.startswith('Hello')
# True

#split() and join()
# Passing split() the argument '\n' lets us split the multiline string
# stored in spam along the newlines and return a list in which each item
# corresponds to one line of the string.
# join()
# >>> ', '.join(['cats', 'rats', 'bats'])
# >>> 'cats, rats, bats'

# Removing Whitespace with strip(), rstrip(), and
# lstrip()
# Sometimes you may want to strip off whitespace characters (space,
# tab, and newline) from the left side, right side, or both sides of a
# string. The strip() string method will return a new string without any
# whitespace characters at the beginning or end. The lstrip() and
# rstrip() methods will remove whitespace characters from the left
# and right ends, respectively. Enter the following into the interactive
# shell:
# >>> spam = ' Hello World '
# >>> spam.strip()
# 'Hello World'
# >>> spam.lstrip()
# 'Hello World '
# >>> spam.rstrip()
# ' Hello World'
# Optionally, a string argument will specify which characters on the
# ends should be stripped. Enter the following into the interactive shell:
# >>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
# >>> spam.strip('ampS')
# 'BaconSpamEggs'
# Passing strip() the argument 'ampS' will tell it to strip occurences of
# a, m, p, and capital S from the ends of the string stored in spam. The
# order of the characters in the string passed to strip() does not
# matter: strip('ampS') will do the same thing as strip('mapS') or
# strip('Spam').