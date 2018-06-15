# script to generate an x,y coordinate plot with variance to simulate a field of crop
# inputs are #row, #columns, distance between the rows and columns, and x & y variance
# output to a CSV file

import csv

numRows = 10
numCols = 15
i = 0
for row in range(numRows):
    for col in range(numCols):
        # print(i)
        # i += 1
