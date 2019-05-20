import re
import os
for filename in os.listdir('./'):
    num = re.match(r'LatinSquare([0-9])_n=([0-9]+)blocked=([0-9]+).lp.png',str(filename)) #finds the value of n.
    if num == None:
        continue
    n = int(num.group(2))
# Image size
    if num.group(1)=="1":
        cmd = "mv "+str(filename)+ " "+ "LatinSquare4_n="+num.group(2)+"blocked="+num.group(3)+".png"
    if num.group(1)=="2":
        cmd = "mv "+str(filename)+ " "+ "LatinSquare6_n="+num.group(2)+"blocked="+num.group(3)+".png"
    if num.group(1)=="3":
        cmd = "mv "+str(filename)+ " "+ "LatinSquare8_n="+num.group(2)+"blocked="+num.group(3)+".png"

    os.system(cmd)
