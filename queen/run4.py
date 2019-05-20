import os
import re
import time
mystring="gringo blocked1.lp supperfastqueens.lp --const n=z | clasp 1"


start=input("Please enter a size of chess bourd: ")

file3=open("data3.txt","w")
filet=open("datat.txt","w")
for number in range(start,start+1):
    for numberblocked in range(1,start*start):
        cout=0
        t=0
        for i in range(0,20):
            mystring=re.sub("z", str(number), mystring)
            cmd="./blocked1 "+str(numberblocked)+" "+str(number)
            os.system(cmd)
            start_time = time.time()  
            x=os.popen(mystring).read() # This will run the command and return any output)
            print len(x)
            print str(x)
            if str(len(x))<="195":
                cout=cout+1
            t=-(start_time-time.time())
            mystring=re.sub(str(start),"z", mystring)
        file3.write(str(numberblocked))
        file3.write("\t")
        file3.write(str(100-cout))
        file3.write("\n")
        filet.write(str(numberblocked))
        filet.write("\t")
        filet.write(str(t))
        filet.write("\n")
    file3.close()
    filet.close()
os.system("gnuplot data3.gnu")
os.system("gnuplot datat.gnu") 
