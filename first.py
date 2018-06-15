# script to generate an x,y coordinate plot with variance to simulate a field of crop
# inputs are #row, #columns, distance between the rows and columns, and x & y variance
# output to a CSV file

import csv

numRows = 10
numCols = 15
i = 0
cordinate = [0,0]
masterlist = []

for row in range(numRows):
    for col in range(numCols):
        cordinate[0] = row
        cordinate[1] = col
        # print(cordinate)
        masterlist.append(cordinate)
        # print(masterlist)
print(masterlist)
plotFile = open('plot.csv')
# exampleReader = csv.reader(exampleFile)
# print(list(exampleReader))

csvWriter = csv.writer(plotFile)
for current in masterlist:
    # csvWriter.writerow(masterlist)
    print(current)

THis is stupid shit that needs undoing
