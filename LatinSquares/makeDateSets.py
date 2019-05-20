import math
from random import randint
import os
import re
from calculateBestEncoding import timeLS

encodings = ["LatinSquare.1.lp","LatinSquare.2.lp","LatinSquare.3.lp","LatinSquare.4.lp","LatinSquare.5.lp","LatinSquare.6.lp",
    "LatinSquare.7.lp","LatinSquare.8.lp"]


for filename in os.listdir("./HardInstances"):
    num = re.match(r'LSn=([0-9]+)blocked=([0-9]+)',str(filename))
    sizeOfBoard = num.group(1)
    numberBlocked = num.group(2)
    times = []
    #times.append(timeLS(" ./encodings/"+encodings[0],numberBlocked,sizeOfBoard)[0])
    #times.append(timeLS(" ./encodings/"+encodings[1],numberBlocked,sizeOfBoard)[0])
    #times.append(timeLS(" ./encodings/"+encodings[2],numberBlocked,sizeOfBoard)[0])
    times.append(timeLS(" ./encodings/"+encodings[3],numberBlocked,sizeOfBoard)[0])
    #times.append(timeLS(" ./encodings/"+encodings[4],numberBlocked,sizeOfBoard)[0])
    times.append(timeLS(" ./encodings/"+encodings[5],numberBlocked,sizeOfBoard)[0])
    #times.append(timeLS(" ./encodings/"+encodings[6],numberBlocked,sizeOfBoard)[0])
    times.append(timeLS(" ./encodings/"+encodings[7],numberBlocked,sizeOfBoard)[0])
    minTime = min(times)
    index = times.index(minTime)
    cmd = "mv ./HardInstances/"+str(filename)+" ./HardInstances/HealdOut/LatinSquare"+str(index+1)+"_n="+str(sizeOfBoard)+"blocked="+str(numberBlocked)+".lp"
    print(cmd)
    os.system(cmd)

