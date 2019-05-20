import os
import re
import time
import multiprocessing


def queen4(numberblocked,start):
    file_name1 = "queens4.lp"
    mystring="gringo ./blocked/blocked" +str(numberblocked)+".lp "+str(file_name1)+ " --const n=" +str(start)+" | clasp 1"
    print(mystring)
    t=0
    start_time = time.time() 
    x=os.popen(mystring).read() # This will run the command and return any outp
    t=-(start_time-time.time())
    return t
    	
#os.system("gnuplot data.gnu")

def queen11(numberblocked,start):
    file_name1 = "queens11.lp"
    mystring="gringo ./blocked/blocked" +str(numberblocked)+".lp "+str(file_name1)+ " --const n=" +str(start)+" | clasp 1"
    print(mystring)
    #cmd="./blocked "+str(numberblocked)+" "+str(number)
    #os.system(cmd)
    start_time = time.time() 
    x=os.popen(mystring).read() # This will run the command and return any outp
    t=-(start_time-time.time())
    return t