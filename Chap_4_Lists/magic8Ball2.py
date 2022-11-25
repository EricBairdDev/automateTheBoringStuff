import random
messages = ['It is certain',
            'It is decidedly so',
            'Reply hazy try again',
            'Yes definitely',
            'Ask again later',
            'Concentrate and try again',
            'My reply is no',
            'Outlook not so good',
            'Very Doubtful']

print(messages[random.randint(0, len(messages) - 1)])


'''EXCEPTIONS TO INDENTATION RULES IN PYTHON
In most cases, the amount of indentation for a line of code tells Python what block
it is in. There are some exceptions to this rule, however. For example, lists can
actually span several lines in the source code file. The indentation of these lines
do not matter; Python knows that until it sees the ending square bracket, the list is
not finished. For example, you can have code that looks like this:
spam = ['apples',
'oranges',
'bananas',
'cats']
print(spam)
Of course, practically speaking, most people use Python’s behavior to make their
lists look pretty and readable, like the messages list in the Magic 8 Ball program.
You can also split up a single instruction across multiple lines using the \ line
continuation character at the end. Think of \ as saying, “This instruction continues
on the next line.” The indentation on the line after a \ line continuation is not
significant. For example, the following is valid Python code:
print('Four score and seven ' + \
'years ago...')
These tricks are useful when you want to rearrange long lines of Python code to
be a bit more readable.'''
