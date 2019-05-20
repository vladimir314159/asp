import os
import time
import matplotlib.pyplot as plt
n=50

time_q4 = []
time_q11 = []
for i in range(2450,2499):
    cmd = "./blocked "+str(i)+ " "+str(n)
    os.system(cmd)
    cmd0 = "gringo queens11.lp blocked.lp --const n="+str(n+10)+" | clasp --time-limit=200 1"
    cmd1 ="gringo queens4.lp blocked.lp --const n="+str(n+10)+" |  clasp --time-limit=200 1"
    start_time = time.time() 
    x=os.popen(cmd0).read() # This will run the command and return any outp
    print(x)
    print(cmd0)
    t=-(start_time-time.time())
    time_q4.append(t)
    start_time = time.time() 
    x=os.popen(cmd1).read() # This will run the command and return any outp
    print(x)
    print(cmd1)
    t=-(start_time-time.time())
    time_q11.append(t)
    print(str(i))
plt.plot(time_q4)
plt.plot(time_q11)
plt.title('Times in transition zone.')
plt.ylabel('time')
plt.xlabel('number blocked')
plt.show()