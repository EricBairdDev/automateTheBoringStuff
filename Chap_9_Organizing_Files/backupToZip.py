#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
    #backup the entire contents of 'folder' into a zip file.
    folder = os.path.abspath(folder) # make sure folder is absolute

    #figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create ZIP file.
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        #add the current folder to the ZIP file.
        backupZip.write(foldername)
        # add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue #dont backup zipfiles
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()

    print('Done.')

backupToZip('C:\\Users\\ericm\\PycharmProjects\\ATBS\\Chap_9_Organizing_Files')