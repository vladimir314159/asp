import csv
import numpy
import operator
import pandas




def MaxQdiagonal(numberfile,sizeofn):
    temp = []
    blocked_file = open("./blocked/blocked"+str(numberfile)+".lp","r")
    listOfBlocked = []
    for line in blocked_file:
        listOfBlocked.append(line)

    for x in listOfBlocked:
        temp.append(x[x.find('(')+1:x.find(')')] )

    listOfBlocked = temp

    #print(listOfBlocked)

    numbers = []
    for el in listOfBlocked:
        numbers.append((int(el[0:el.find(',')])-1,int(el[el.find(',')+1:len(el)])-1))

    count = [0]*sizeofn*2
    #print(numbers)
    for i in range(0,sizeofn):
        for j in range(0,sizeofn):
            if (i,j) in numbers:
                    count[i+j]+=1

    #print(count)
    for i in range(0,sizeofn):
        count[i]=i*(count[i]/(i+1)) #weighted
        count[2*sizeofn-1-i]=(2*sizeofn-i) * count[2*sizeofn-1-i]/(i+1) #weighted
    #print( numpy.mean(count) )
    print(count)
    a = max(count, key=lambda x: x) / ( sizeofn*2 )
    return a
#print(MaxQdiagonal(2016,50))