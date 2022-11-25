#! python 3
# pw.py - An insecure password locker program.
import sys

PASSWORDS = {'email': 'f7B9l2089',
             'blog': 'AA198198Sa',
             'luggage': '298dhi328hD#2'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
