#! python3
# mapIt.py - launches a map in the berowser using an address from the command line or clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

# import requests
# res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
# try:
#   res.raise_for_status()
# except Exception as exc:
#   print('There was a problem: %s' % (exc))
# ^^^^^ to handle res.raise_for_status() without crashing