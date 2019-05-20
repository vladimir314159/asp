import csv
import numpy
import operator
import pandas as pd
from CreateRandomSubBoard import CreateRandomSubBoard
from calculateBestEncoding import queen11, queen4
from statistics import mean

csv_input = pd.DataFrame()
#csv_input = pd.read_csv("input.csv")

numberqueens = 50

fullBoardWinner = []

"""
for number in range (5600,5700):
   MaxQdiagonal_array.append( MaxQdiagonal(number,numberqueens) )
"""

for number in range (1,2500):
    if queen4(number,numberqueens,False)[1] == 1:
        fullBoardWinner.append("SAT")
    else:
        fullBoardWinner.append("UnSAT")



csv_input['Satisfiable?'] = fullBoardWinner
#csv_input['winer'] = queens_encoding_array

#csv_input['MaxQdiagonal'] = MaxQdiagonal_array

csv_input.to_csv('out1.csv', index=False)
