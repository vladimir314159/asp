import os

start=input("Please enter the start blocked: ")

end=input("Please enter the end blocked: ")

size=input("Please enter size of bord: ")


for i in range (start, end+1):
    cmd="./blocked "+str(i)+ " "+str(size)
    os.system(cmd)
    print "finished number: "+str(i)
    cmd2="mv blocked.lp "+"blocked"+str(i)+".lp"
    os.system(cmd2)
