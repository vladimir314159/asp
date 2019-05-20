import os

n = 80
f = open("blocked.lp","w")

for i in range (1, n+1):
    for j in range (1, n+1):
        f.write("blocked("+str(i)+","+str(j)+").\n")
