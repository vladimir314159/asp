import os
import re
import time
import multiprocessing

s=input("Start: ")
e=input("End: ")
start=input("Please enter a size of chess bourd: ")

def queen4(start,numberblocked):
	file_name1="queens4.lp" 
	file_name="queens4.txt"
	file3=open(file_name,"a")
	print file_name
	mystring="gringo blocked" +str(numberblocked)+".lp "+str(file_name1)+ " --const n=" +str(start)+" | clasp 1"
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
        file3.write(str(numberblocked))
        file3.write("\t")
    	file3.write(str(t))
	file3.write("\n")   
	file3.close()
#os.system("gnuplot data.gnu")

def queen11(start,numberblocked):
	file_name1="queens11.lp" 
	file_name="queens11.txt"
	file3=open(file_name,"a")
	mystring="gringo blocked" +str(numberblocked)+".lp "+str(file_name1)+ " --const n=" +str(start)+" | clasp 1"
	print file_name
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
	file3.write(str(numberblocked))
    	file3.write("\t")
    	file3.write(str(t))
	file3.write("\n")   
	file3.close()

#os.system("gnuplot data.gnu")

if __name__=='__main__':
 # Start bar as a process
    	number=0
	for number in range(start,start+1):
    #mystring=re.sub("z", str(number), mystring)
    #print mystring
		for numberblocked in range(s,e+1):       
			p = multiprocessing.Process(target=queen4(number, numberblocked))
			p.start()
			# Wait for 10 seconds or until process finishe
			p.join(10)
			# If thread is still active
			if p.is_alive():
			        print "Stoping queens4.lp goint to run queens11.lp"
			        # Terminate
			        p.terminate()
			        p.join()
			else:
				continue
			d = multiprocessing.Process(target=queen11(number, numberblocked))
			d.start()
			d.join(30)
			if d.is_alive():
				print "Stoping queens11.lp going to run queens11.lp"
				d.terminate()
				d.join()
			else:
				continue
			p.start()
