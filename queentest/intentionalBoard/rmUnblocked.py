import os


f = open("unblock","r")

line = f.readline()

while line:
    line = line.rstrip()
    a = str(line)
    print(a)
    cmd = "sed -i '/"+a+"/d' blocked.lp"
    os.system(cmd)
    line = f.readline()
    