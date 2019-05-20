from random import randint
import math
import os
from subprocess import call
import pandas as pd
from CreateRandomSubBoard import CreateRandomSubBoard
from calculateBestEncoding import queen11, queen4
import numpy as np
from numpy import array

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

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
answer4 = []
### This makes blocked 
csv_input = pd.DataFrame()
NumberOfExamples = 100

for i in range(NumberOfExamples):
    print(i)
    sizeOfBoard = randint(60,80)
    n_squared = sizeOfBoard**2
    numberBlocked_range = (math.ceil(n_squared*0.81),math.ceil(n_squared*0.92))
    numberBlocked = randint(numberBlocked_range[0],numberBlocked_range[1])
    filename = "./blocked/blocked_n="+str(sizeOfBoard)+"_"+str(numberBlocked)
    cmd = '( cd ./blocked && ./blocked '+str(numberBlocked)+' '+str(sizeOfBoard)+' )'
    os.system(cmd)
    cmd = "mv ./blocked/blocked.lp "+filename
    os.system(cmd)
    ####################
    ####################
    ####################
   



#csv_input = pd.read_csv("input.csv")
    for i in range(50):
        CreateRandomSubBoard(filename,numberBlocked,sizeOfBoard,math.ceil(sizeOfBoard/1.6))
        b, a = queen11(filename,numberBlocked,math.ceil(sizeOfBoard/1.6),True)
        time11.append(b)
        b, a = queen4(filename,numberBlocked,math.ceil(sizeOfBoard/1.6),True)
        time4.append(b), answer4.append(a)
        if  time11[i] <= time4[i]:
            print("queen11")
            queens_encoding_array.append("queen11")
        else:
            print("queen4")
            queens_encoding_array.append("queen4")
    time4_long.append(queen4(filename,numberBlocked,sizeOfBoard,False))
    time11_long.append(queen11(filename,numberBlocked,sizeOfBoard,False))
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
    n_array.append(sizeOfBoard)
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
csv_input.to_csv('data_transition_1.csv', index=False)



