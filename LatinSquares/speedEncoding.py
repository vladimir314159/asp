import os
import re
import matplotlib.pyplot as plt
import time
import itertools as it
time1 = []
time2 = []
time3 = []
time4 = []
time5 = []
time6 = []
time7 = []
time8 = []
for j in range(1,100):
    print(j)
    for i in it.chain(range(1,3),range(5,7)):
        command = "clingo encodings/LatinSquare."+str(i)+".lp --const n="+str(j)+" 1"
        start_time = time.time()
        print(command)
        x=os.popen(command).read() # This will run the command and return any outp
        t=-(start_time-time.time()) 
        if i == 1:
            time1.append(t)
        if i == 2:
            time2.append(t)
        if i == 3:
            time3.append(t)
        if i == 4:
            time4.append(t)
        if i == 5:
            time5.append(t)
        if i == 6:
            time6.append(t)
        if i == 7:
            time7.append(t)
        if i == 8:
            time8.append(t)
print("time1\t",time1)
print("time2\t",time2)
plt.plot(time1)
plt.plot(time2)
plt.plot(time3)
plt.plot(time4)
plt.plot(time5)
plt.plot(time6)
plt.plot(time7)
plt.plot(time8)
plt.title('predictions')
plt.ylabel('time')
plt.xlabel('instaince')
plt.legend(['time1', 'time2','time3','time4','time5','time6','time7','time8'], loc='upper left')
image_name = "Predictions-cnn.png"
plt.savefig(image_name)
plt.clf()
plt.cla()
plt.close()
plt.show()