import os
import re
import time
import multiprocessing

def checksolution(x):
    print(x)
    if len(x) >= 195:
        return 1
    return 0

def queen4(numberblocked,start,sub):
    file_name1 = "queens4.lp"
    if sub:
        mystring="gringo ./blocked"+str(numberblocked)+"/blockedSub.lp "+str(file_name1)+" --const n=" +str(int(start))+" | clasp 1"
    else:
        mystring="gringo ./HealdOutSet/encodings/blocked.lp "+str(file_name1)+" --const n=" +str(int(start))+" | clasp 1"
    print(mystring)
    t=0
    start_time = time.time() 
    x=os.popen(mystring).read() # This will run the command and return any outp
    t=-(start_time-time.time())
    return t, checksolution(x)
    	
#os.system("gnuplot data.gnu")

def queen11(numberblocked,start,sub):
    file_name1 = "queens11.lp"
    if sub:
        mystring="gringo ./blocked"+str(numberblocked)+"/blockedSub.lp "+str(file_name1)+" --const n=" +str(int(start))+" | clasp 1"
    else:
        mystring="gringo ./HealdOutSet/encodings/blocked.lp "+str(file_name1)+" --const n=" +str(int(start))+" | clasp 1"
    print(mystring)
    #cmd="./blocked "+str(numberblocked)+" "+str(number)
    #os.system(cmd)
    start_time = time.time() 
    x=os.popen(mystring).read() # This will run the command and return any outp
    t=-(start_time-time.time())
    return t, checksolution(x)