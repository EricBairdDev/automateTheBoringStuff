#1 python3
# readCensusExcel.py - Tabulates population and number of census tracts for each county

import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

#TODO: Fill in countyData with each county's pop and tracts