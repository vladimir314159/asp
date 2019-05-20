import os
import re
import time

s=input("start: ")
e=input("end: ")

file_number=input("Please enter a queen?.lp file: ")
file_number2=input("Plase enter a queen?.lp file: ")
#file_number3=input("Please enter a queen?.lp file: ")


file_name="queens"+str(file_number) 
file_name2="queens"+str(file_number2)
#file_name3="queens"+str(file_number3)

mystring="gringo blocked.lp "+str(file_name)+ ".lp --const n=z | clasp 1"
mystring2="gringo blocked.lp "+str(file_name2)+ ".lp --const n=z | clasp 1"
#mystring3="gringo blocked.lp "+str(file_name3)+ ".lp --const n=z | clasp 1"

start=input("Please enter a size of chess bourd: ")
file_name=file_name+ ".txt"
file_name2=file_name2+".txt"
#file_name3=file_name3+".txt"

file3=open(file_name,"w")
file4=open(file_name2,"w")
#file5=open(file_name3,"w")
print file_name
for number in range(start,start+1):
    mystring=re.sub("z", str(number), mystring)
    mystring=re.sub("z", str(number), mystring2)
#    mystring=re.sub("z", str(number), mystring3)
    print mystring
    for numberblocked in range(s,e):
        cout=0 
        t=0
        cmd="./blocked "+str(numberblocked)+" "+str(number)
        os.system(cmd)
        start_time = time.time() 
        x=os.popen(mystring).read() # This will run the command and return any outp
        t=-(start_time-time.time())
        start_time1 = time.time() 
        y=os.popen(mystring2).read()
        u=-(start_time1-time.time())
#        start_time2 = time.time() 
#        z=os.popen(mystring3).read()
#        v=-(start_time2-time.time())
        if len(x)<=195:
            print "No solution time encoding  1: "+ str(t)
        else:
            print "Yes solution time encoding 1: "+ str(t)

        if len(y)<=195:
            print "No solution time encoding  2: "+ str(u)
        else:
            print "Yes solution time encoding 2: "+ str(u)

#        if len(z)<=195:
#            print "No solution time encoding  3: "+ str(v)
#        else:
#            print "Yes solution time encoding 3: "+ str(v)
        file3.write(str(numberblocked))
        file3.write("\t")
        file3.write(str(t))
        file3.write("\n")

        file4.write(str(numberblocked))
        file4.write("\t")
        file4.write(str(u))
        file4.write("\n")

#        file5.write(str(numberblocked))
#        file5.write("\t")
#        file5.write(str(v))
#        file5.write("\n")       
    file3.close()
    file4.close()
#    file5.close()
os.system("gnuplot data.gnu") 
