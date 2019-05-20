import os
import time
import matplotlib.pyplot as plt
import numpy as np
time_solved = []
ratio_solved = []
x_cords = []
f = open("data.txt","w")

for i in range(3920,4700,5):
    x_cords.append(i)
    print(i)
    times = []
    ratios = []
    for j in range(30):
        cmd="./blocked "+str(i)+ " "+str(70)
        os.system(cmd)
        mystring="gringo blocked1.lp queens4.lp --const n=70 | clasp --time-limit=180 1"
        start_time = time.time()
        x=os.popen(mystring).read() # This will run the command and return any outp
        #print(x) 
        t=abs(start_time-time.time())
        if t >=200:
            continue
        ratios.append(t/80)
        if len(x)<=195:
            print ("No."+ str(t))
            times.append(0)
        else:
            print( ("Yes."+ str(t)))
            print(times)
            times.append(1)
    f.write(str(np.mean(time_solved)))
    f.write(",")
    f.write(str(np.mean(ratio_solved)))
    f.write("\n")
    ratio_solved.append(np.mean(times))
    time_solved.append(np.mean(ratios))
plt.plot(x_cords,time_solved,'r')
plt.plot(x_cords,ratio_solved,'b')
plt.show()
