#! python3
# renameDates.py - Renames filenames with American MM-DD-YYY date format to European DD-MM-YYY

import shutil, os, re

# create regex that matches files with the American date format.

datePattern = re.compile(r"""^(.*?) #text before date
((0|1)?\d)-         #one or two digits for the month
((0|1|2|3)?\d)-     # one or two digits for the day
((19|20)\d\d)       # four digits for the year
(.*?)$              # All the text after the date
""", re.VERBOSE)

# TODO: Loop over the files in the working directory.
# TODO: Skip files without a date.
# TODO: Get the different parts of the filename.
# TODO: Form the European-style filename.
# TODO: Get the full, absolute file paths.
# TODO: Rename the files.