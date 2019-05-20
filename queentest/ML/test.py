import re
import os

for filename in os.listdir('./HealdOutSet'):
    num = re.match(r'queen([0-9]+)[a-z0-9\.]*_n=([0-9]*)_[0-9]+\.png',str(filename)) #finds the value of n.
    print(num)
    if num != None:
        print(num.group(1)+"\t"+num.group(2))
