import os
import re
import time

file_number=input("Please enter a queen?.lp file: ")
s=input("Start: ")
e=input("End: ")

file_name1="queens"+str(file_number) 

short=" --text | wc -w"

start=input("Please enter a size of chess bourd: ")
file_name=file_name1+ ".txt"
file3=open(file_name,"w")
print file_name
for number in range(start,start+1):
    #mystring=re.sub("z", str(number), mystring)
    #print mystring
    for numberblocked in range(s,e+1):
        mystring="gringo blocked" +str(numberblocked)+".lp "+str(file_name1)+ ".lp --const n=" +str(start)+" | clasp 1"
        mystring1="gringo blocked" +str(numberblocked)+".lp "+str(file_name1)+ ".lp --const n=" +str(start)+str(short)
        print mystring
        cout=0 
        t=0
        #cmd="./blocked "+str(numberblocked)+" "+str(number)
        #os.system(cmd)
        start_time = time.time() 
        x=os.popen(mystring).read() # This will run the command and return any outp
        t=-(start_time-time.time())
        if len(x)<=195:
            print "No solution time: "+ str(t)
        else:
            print "Yes solution time: "+ str(t)
        count=os.popen(mystring1).read()
        file3.write(str(numberblocked))
        file3.write("\t")
        file3.write(str(t))
        file3.write("\t")
        file3.write(str(count))       
    file3.close()
#os.system("gnuplot data.gnu")
 
