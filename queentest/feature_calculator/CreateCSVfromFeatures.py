import csv
import numpy
import operator
import pandas as pd
from MaxQcol import MaxQcol
from AvgQdiagonal import MaxQdiagonal
from MaxQrow import MaxQrow
from calculateBestEncoding import queen11, queen4
from LongestnotQseqCol import LongestC
from LongestnotQseqRow import LongestR

csv_input = pd.DataFrame()
#csv_input = pd.read_csv("input.csv")

numberqueens = 70
Longestblocked_row = []
Longestblocked_col = []
MaxQcol_array = []
MaxQdiagonal_array = []
MaxQrow_array = []
blockednsq_array = []
n_array = []
queens_encoding_array = []

"""
for number in range (5600,5700):
   MaxQdiagonal_array.append( MaxQdiagonal(number,numberqueens) )
"""

for number in range (4300,4360):
    Longestblocked_col.append(LongestC(number, numberqueens)[0])
    Longestblocked_row.append(LongestR(number,numberqueens)[0])
    """
    MaxQcol_array.append( MaxQcol(number,numberqueens)[1])
    MaxQdiagonal_array.append( MaxQdiagonal(number,numberqueens))
    MaxQrow_array.append( MaxQrow(number,numberqueens)[1])
    blockednsq_array.append( number / (numberqueens * numberqueens)  )
    n_array.append(numberqueens)

    if queen11(number,numberqueens) <= queen4(number,numberqueens):
        print("queen11")
        queens_encoding_array.append("queen11")
    else:
        print("queen4")
        queens_encoding_array.append("queen4")
    """

"""
csv_input['MaxQcol'] = MaxQcol_array
csv_input['MaxQrow'] = MaxQrow_array

csv_input['blocked/n^2'] = blockednsq_array
csv_input['n'] = n_array
csv_input['class'] = queens_encoding_array
"""

#csv_input['MaxQdiagonal'] = MaxQdiagonal_array
csv_input.insert(0,'LongestBC',Longestblocked_col)
csv_input.insert(1,'LognestBR',Longestblocked_row)

csv_input.to_csv('data_rowcol.csv', index=False)
