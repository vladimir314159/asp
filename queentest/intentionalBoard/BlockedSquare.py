import re
import os
import math
import time
from random import randrange, uniform
import subprocess

def BlockedSquare(sizeofBoard,sizeofBlocked):
    fromright = sizeofBoard-sizeofBlocked
    fromtop = sizeofBoard-sizeofBlocked
    n_squared = sizeofBlocked*sizeofBlocked
    numBlocked = randrange(math.ceil(n_squared*0.88),math.ceil(n_squared))
    print(numBlocked)
    cmd = './blocked '+str(numBlocked)+' '+str(sizeofBlocked)
    print(cmd)
    subprocess.run(['./blocked',str(numBlocked),str(sizeofBlocked)])
    fp1 = open('blocked1.lp','w')
    fp = open('blocked.lp','r')
    for line in fp:
        a = line.find("(")
        b = line.find(",")
        c = line.find(")")
        thingtowrite = "blocked("+str(int(line[a+1:b])+fromright)+","+str(int(line[b+1:c])+fromtop)+").\n"
        #print(thingtowrite)
        fp1.write(thingtowrite)
    cmd1 = "mv blocked1.lp ./datasetI/blocked_n="+str(sizeofBoard)+"_"+str(sizeofBlocked)+"_"+str(numBlocked)
    print(cmd1)
    os.system(cmd1)
    

for i in range(500):
    size = randrange(50,85)
    BlockedSquare(size,math.ceil((2*size)/4))
