import csv
from numpy import array
import operator
import pandas as pd
from CreateRandomSubBoard import CreateRandomSubBoard
from calculateBestEncoding import queen11, queen4
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


csv_input = pd.DataFrame()
#csv_input = pd.read_csv("input.csv")

numberqueens = 70

fullBoardWinner = []
MaxQcol_array = []
MaxQdiagonal_array = []
MaxQrow_array = []
blockednsq_array = []
n_array = []
queens_encoding_array = []
time11_array = []
time4_array =[]
answer = []
time = []
time11 = []
time4 = []
time4_long = []
time11_long = []
satorUnsat = []
"""
for number in range (5600,5700):
   MaxQdiagonal_array.append( MaxQdiagonal(number,numberqueens) )
"""

for number in range (3700,4900):
    answer4 = []
    for i in range(10):
        CreateRandomSubBoard(number,numberqueens,numberqueens/2)
        b, a = queen11(number,numberqueens/2,True)
        time11.append(b)
        b, a = queen4(number,numberqueens/2,True)
        time4.append(b), answer4.append(a)
        if  time11[i] <= time4[i]:
            print("queen11")
            queens_encoding_array.append("queen11")
        else:
            print("queen4")
            queens_encoding_array.append("queen4")
    time4_long.append(queen4(number,numberqueens,False))
    time11_long.append(queen11(number,numberqueens,False))
    if  time4_long[-1][0] > time11_long[-1][0]:
        fullBoardWinner.append("queen11")
    else:
        fullBoardWinner.append("queen4")
    if time4_long[-1][1] == 1:
        satorUnsat.append("SAT")
    else:
        satorUnsat.append("UnSAT")
    time11_array.append(mean(time11))
    time4_array.append(mean(time4))
    n_array.append(numberqueens)
    print(answer4)
    answer.append(mean(answer4))

#csv_input['blocked/n^2'] = blockednsq_array
csv_input['time4sub'] = time4_array
csv_input['time11sub'] = time11_array
csv_input['solution?'] = answer
csv_input['n']= n_array
csv_input['time4'] = array(time4_long)[:,0]
csv_input['time11'] = array(time11_long)[:,0]
csv_input['correct winner'] = fullBoardWinner
csv_input['SAT?'] = satorUnsat
#csv_input['winer'] = queens_encoding_array
#csv_input['MaxQdiagonal'] = MaxQdiagonal_array
csv_input.to_csv('data70.csv', index=False)