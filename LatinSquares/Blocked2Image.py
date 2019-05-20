#!/usr/bin/env python

import scipy.misc
import numpy as np
import os
import re
#size of n will determine width and height.

widths = []
heights = []
files = []
ns = []

for filename in os.listdir('./HealdOutSet'):
    num = re.match(r'LatinSquare[0-9]_n=([0-9]+)blocked=([0-9]+).lp',str(filename)) #finds the value of n.
    if num == None:
        continue
    files.append(str(filename))
    n = int(num.group(1))
    ns.append(n)
# Image size
    widths.append( n*10  )       
    heights.append( n*10 )
channels = 3




# Create an empty image

# Draw something (http://stackoverflow.com/a/10032271/562769)
#xx, yy = np.mgrid[:height, :width]
#circle = (xx - 100) ** 2 + (yy - 100) ** 2
print(files)
# Set the RGB values
for number in range (len(files)):
    print(number)
    width = widths[number]
    height = heights[number]
    n = ns[number]
    img = np.zeros((height, width, channels), dtype=np.uint8)
    blocked_file = open("./HealdOutSet/"+files[number],"r")
    listOfBlocked = []
    for line in blocked_file:
        listOfBlocked.append(line)
    print(listOfBlocked)
    temp = []

    for x in listOfBlocked:
        temp.append(x[x.find('(')+1:x.find(')')] )
    listOfBlocked = temp

    #print(listOfBlocked)

    numbers = []
    shades = []
    listOfBlocked.pop(0)
    #print("listOfBlocked\t:",listOfBlocked)
    for el in listOfBlocked:
       # numberssss.append((int(el[0:el.find(',')])-1,int(el[el.find(',')+1:len(el)])-1))
        s = [int(x) for x in el.split(',')]
        print("s:",s)
        numbers.append((s[0],s[1]))
        shades.append(s[2])
    print("numbers:\t",numbers)

    #print(numbers)
    #listOfBlocked = numbers
        
    #print(img.shape)          

    r0, g0, b0 = 0, 0, 0
    r1, g1, b1 = 255, 255, 255  #should be 255

    def isQueen(mylist, numberofqueens):
        temp_height = []
        temp_width = []
        for i in range(0,height):
            temp_height.append((i/numberofqueens)*height)
        for i in range(0,width):
            temp_width.append((i/numberofqueens)*width)
        return (temp_height, temp_width)

    count = 0
    listOfBlocked = numbers
    for y in range(0,img.shape[0],10):
        for x in range(0,img.shape[1],10): 
            blocked = ((int(y / 10) +1),(int(x / 10) +1))
            #print(len(blocked))
            #print(blocked)
            #print(listOfBlocked)
            if blocked in listOfBlocked:
                index = listOfBlocked.index(blocked)
                shade = shades[index]
                #print("T")
                count+=1
                for i in range(10):
                    for j in range(10):
                        img[y+i][x+j][0] = (255/n)*shade
                        img[y+i][x+j][1] = (255/n)*shade
                        img[y+i][x+j][2] = (255/n)*shade
            else:
                #print("F")
                for i in range(10):
                    for j in range(10):
                        img[y+i][x+j][0] = r1
                        img[y+i][x+j][1] = 0
                        img[y+i][x+j][2] = b1
    # Display the imagels -lsa | grep -E "[d\-](([rw\-]{2})x){1,3}"
    #print(count)
    # Save the image
    scipy.misc.imsave("./HealdOutSet/pictures/"+str(files[number])+".png", img)