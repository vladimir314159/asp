import os
import re
import time
import multiprocessing

s=input("Start: ")
e=input("End: ")
start=input("Please enter a size of chess bourd: ")

def queen4(start,numberblocked,TIMEOUT):
    file_name1="queens4.lp"
    file_name="diff.txt"
    file3=open(file_name,"a")
    mystring="gringo blocked" +str(numberblocked)+".lp "+str(file_name1)+ " --const n=" +str(start)+" | clasp 1"
    print(mystring)
    t=0
    #cmd="./blocked "+str(numberblocked)+" "+str(number)
    #os.system(cmd)
    start_time = time.time()
    x=os.popen(mystring).read() # This will run the command and return any outp
    t=abs(start_time-time.time())
    if len(x)<=195:
        print "No solution time: "+ str(t)
    else:
        print( ("Yes solution time: "+ str(t)))
    if t<TIMEOUT:
        file3.write(str(numberblocked))
        file3.write("\t")
        file3.write(str(t))
        file3.write("\n")
        file3.close()
    else:
        file3.close()
#os.system("gnuplot data.gnu")

def queen11(start,numberblocked,temp):
    file_name1="queens11.lp"
    file_name="diff.txt"
    file3=open(file_name,"a")
    mystring="gringo blocked" +str(numberblocked)+".lp "+str(file_name1)+ " --const n=" +str(start)+" | clasp 1"
    print mystring
    t=0
    #cmd="./blocked "+str(numberblocked)+" "+str(number)
    #os.system(cmd)
    start_time = time.time()
    x=os.popen(mystring).read() # This will run the command and return any outp
    t=temp+abs(start_time-time.time())
    if len(x)<=195:
        print "No solution time: "+ str(t)
    else:
        print "Yes solution time: "+ str(t)
    file3.write(str(numberblocked))
    file3.write("\t")
    file3.write(str(t))
    file3.write("\n")
    file3.close()

#os.system("gnuplot data.gnu")

if __name__=='__main__':
 # Start bar as a process
    TIMEOUT=10
    os.system("rm diff.txt")
    number=0
    for number in range(start,start+1):
    #mystring=re.sub("z", str(number), mystring)
    #print mystring
        for numberblocked in range(s,e+1):
            p_create_time=time.time()
            p = multiprocessing.Process(target=queen4(number, numberblocked,TIMEOUT))
            p.start()
            p.join(TIMEOUT)
            p.terminate()
        #    while i==0:
        #       if abs(time.time() - p_create_time) >= TIMEOUT:
                    #cmd = "kill "+str(p.pid)
                    #print cmd
                    #os.system(cmd)
        #           p.terminate()
        #           i=1
         #          continue
         #      if not p.is_alive():
         #          i=2
         #  print str(i)
            t = abs(time.time()-p_create_time)
            if t>=TIMEOUT:
                print str(t)
                print "Stoped queens4.lp starting queens11.lp"
                d = multiprocessing.Process(target=queen11(number,numberblocked,TIMEOUT))
                d.start()
