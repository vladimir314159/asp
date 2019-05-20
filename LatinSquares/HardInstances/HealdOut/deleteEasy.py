import re
import os
import time

for filename in os.listdir('./'):
    num = re.match(r'[A-Za-z0-9_]+n=([0-9]*)blocked=([0-9]+)\.lp',str(filename)) #finds the value of n.
    print("Num",num)
    if num is None:
        continue
    sizeofboard = num.group(1)
    print("filename:\t"+filename)
    
    mystring="gringo ../../encodings/LatinSquare.4.lp ./"+str(filename) +" --const n="+str(sizeofboard)+" |  clasp --time-limit=5 1"
    print(mystring)
    t=0
    start_time = time.time() 
    x=os.popen(mystring).read() # This will run the command and return any outp
    t=-(start_time-time.time())   
    x = x.replace('\n', ' ').replace('\r', '')
    if t >=4:
        print("good")
        continue
    cmd = "rm "+filename
    print(cmd)
    os.system(cmd)

