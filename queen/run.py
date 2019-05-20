import os
import re
import time
mystring="gringo queens.lp --const n=z | clasp 1"

start=input("Please enter a place to start: ")
end= input("Please enter a place to end: ")


file1=open("data.txt","w")

for i in range(start,end):
    mystring=re.sub("z", str(i), mystring)
    start_time = time.time()
    os.system(mystring) # run command
    os.popen(mystring).read() # This will run the command and return any output
    t=-(start_time-time.time())/2
    mystring=re.sub(str(i),"z", mystring)
    file1.write(str(i))
    file1.write("\t")
    file1.write(str(t))
    file1.write("\n")
file1.close()
os.system("gnuplot data.gnu")

