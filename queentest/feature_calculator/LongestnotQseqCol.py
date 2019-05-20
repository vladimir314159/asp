import csv
import numpy
import operator
import pandas





def LongestC(filenumber, sizeofn):
    temp = []
    listOfBlocked = []
    blocked_file = open("./blocked/blocked"+str(filenumber)+".lp","r")
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
    #print(numbers)
    count = [0]*sizeofn
    #print(count)
    previous_element = (-1,-1)
    for i in range(0,len(numbers)):
        if numbers[i][0] == previous_element[0]+1:
            count[ numbers[i][1] ] += 1
        previous_element = numbers[i]
    #print("sour creme")
    #print(count)
    max_el = max(count, key=lambda x: x)
    #print(max_el)
    return max_el/sizeofn , sum(count)
print(LongestC(6001,80))