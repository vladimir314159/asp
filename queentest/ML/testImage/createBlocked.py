import math
from random import randint
import os
from calculateBestEncoding import queen11, queen4

"""
n = 60
for i in range(1,n*n):
    numberBlocked = i
    winner = "queen4"
    if queen11(i,n,False)[0] < queen4(i,n,False)[0]:
        winner = "queen11"
    filename = "./datasetI/"+winner+".blocked_n="+str(n)+"_"+str(numberBlocked)
    cmd = '( cd ./datasetI && ./blocked '+str(numberBlocked)+' '+str(n)+' )'
    os.system(cmd)
    cmd = "mv ./datasetI/blocked.lp "+filename
    os.system(cmd)
"""

for i in range(1):
    #sizeOfBoard = randint(60,80)
    sizeOfBoard = 67
    n_squared = sizeOfBoard**2
    for j in range (math.ceil(n_squared*0.81),math.ceil(n_squared*0.92)):
        numberBlocked = j
        cmd = '( cd ./datasetI && ./blocked '+str(numberBlocked)+' '+str(sizeOfBoard)+' )'
        os.system(cmd)
        winner = "queen4"
        if queen11(j,sizeOfBoard,False)[0] < queen4(j,sizeOfBoard,False)[0]:
            winner = "queen11"
        filename = "./datasetI/"+winner+".blocked_n="+str(sizeOfBoard)+"_"+str(numberBlocked)
        cmd = "mv ./datasetI/blocked.lp "+filename
        os.system(cmd)
