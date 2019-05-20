import os
import re
import time
import multiprocessing

def checksolution(x):
    print(x)
    if len(x) >= 195:
        return 1
    return 0

def timeLS(encodingName,numberblocked,sizeOfBoard):
    mystring="gringo ./HardInstances/LSn="+str(sizeOfBoard)+"blocked="+str(numberblocked)+".lp"+encodingName+" --const n="+str(sizeOfBoard)+" |  clasp --time-limit=200 1"
    print(mystring)
    t=0
    start_time = time.time() 
    x=os.popen(mystring).read() # This will run the command and return any outp
    t=-(start_time-time.time())
    return t, checksolution(x)
    	
