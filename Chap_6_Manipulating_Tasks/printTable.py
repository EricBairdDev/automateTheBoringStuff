def printTable(list):
    colWidths = [0] * len(list)
    for i in range (len(list)):
        colWidths[i]= (len(max(list[i], key=len)))
    for x in range(4):
	    for y in range(len(list)):
		    print(list[y][x].rjust(colWidths[y]+1), end='')
	    print(' ')





    #TODO:


tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)