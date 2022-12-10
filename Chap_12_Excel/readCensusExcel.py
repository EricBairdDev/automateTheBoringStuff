#1 python3
# readCensusExcel.py - Tabulates population and number of census tracts for each county

import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

#TODO: Fill in countyData with each county's pop and tracts
print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one sensus tract
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

#TODO: Open a new text file and write the contents of countyData to it