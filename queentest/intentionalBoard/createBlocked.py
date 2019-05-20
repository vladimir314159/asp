import math
from random import randint
import os
import re
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

n = 0
blocked = 0
files = []
for filename in os.listdir('./datasetI'):
    print(filename)
    files.append(filename)
    num = re.match(r'blocked_n=([0-9]+)_[0-9]+_([0-9]+)',str(filename)) #finds the value of n.
    print(num)
    if num != None:
        print(num.group(1)+"\t"+num.group(2))

n = num.group(1)
blocked = num.group(2)


for afile in files:
    print(afile)
    num = re.match(r'blocked_n=([0-9]+)_[0-9]+_([0-9]+)',str(afile))
    n = num.group(1)
    blocked = num.group(2)
    winner = "queen4"
    if queen11(blocked,n,False,"./datasetI/"+afile)[0] < queen4(blocked,n,False,"./datasetI/"+afile)[0]:
        winner = "queen11"
    filename = "./datasetI/"+winner+".blocked_n="+str(n)+"_"+str(blocked)
    mycmd = "mv ./datasetI/"+str(afile)+" "+filename
    print(mycmd)
    os.system(mycmd)

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
"""