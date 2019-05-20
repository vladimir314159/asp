import csv
import numpy
import operator
import pandas
import os
from random import randint





def CreateRandomSubBoard(filenumber, sizeofn, dimisionsBoard):
    temp = []
    listOfBlocked = []
    blocked_file = open("./blocked"+str(filenumber)+".lp","r")
    for line in blocked_file:
        listOfBlocked.append(line)

    for x in listOfBlocked:
        temp.append(x[x.find('(')+1:x.find(')')] )

    listOfBlocked = temp
    #print(listOfBlocked)
    numbers = []
    for el in listOfBlocked:
        numbers.append((int(el[0:el.find(',')])-1,int(el[el.find(',')+1:len(el)])-1))
    #sorted(numbers, key=lambda numbers: numbers[0]) #this sorts by first element in the list
    numbers.sort(key=operator.itemgetter(1,0))  
    beginSub_0 = randint(0, (sizeofn - 1) - dimisionsBoard)
    endSub_0 = beginSub_0 + dimisionsBoard -1
    beginSub_1 = randint(0, (sizeofn - 1) - dimisionsBoard)
    endSub_1 = beginSub_1 + dimisionsBoard -1
    SubBoard = []
    for x in numbers:
        if beginSub_0 <= x[0] <= endSub_0:
            if beginSub_1 <= x[1] <= endSub_1:
                SubBoard.append(x)
    filename = "./blocked"+str(filenumber)+"/blockedSub.lp" #+"("+str(beginSub_0)+","+str(endSub_0)+")"+"by"+"("+str(beginSub_1)+","+str(endSub_1)+")"
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    f = open(filename,"w")
    for x in SubBoard:
        #print("blocked("+str(x[0]-(beginSub_0-1))+","+str(x[1]-(beginSub_1-1))+").\n")
        f.write("blocked("+str(x[0]-(beginSub_0-1))+","+str(x[1]-(beginSub_1-1))+").\n") #not this shifts the things
    print("("+str(beginSub_0)+","+str(endSub_0)+")")
    print("("+str(beginSub_1)+","+str(endSub_1)+")")  
    f.close()
    #print(SubBoard)
#print(CreateRandomSubBoard(3459,70,20))