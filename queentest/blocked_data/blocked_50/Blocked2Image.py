#!/usr/bin/env python

import scipy.misc
import numpy as np

# Image size

channels = 3
n = 50
width = 10*n
height = 10*n
# Create an empty image
img = np.zeros((height, width, channels), dtype=np.uint8)
# Draw something (http://stackoverflow.com/a/10032271/562769)
#xx, yy = np.mgrid[:height, :width]
#circle = (xx - 100) ** 2 + (yy - 100) ** 2

# Set the RGB values
for number in range (2300,2301):
    blocked_file = open("./blocked"+str(number)+".lp","r")
    listOfBlocked = []
    for line in blocked_file:
        listOfBlocked.append(line)


    temp = []

    for x in listOfBlocked:
        temp.append(x[x.find('(')+1:x.find(')')] )
    listOfBlocked = temp

    #print(listOfBlocked)

    numbers = []
    for el in listOfBlocked:
        numbers.append((int(el[0:el.find(',')])-1,int(el[el.find(',')+1:len(el)])-1))

    #print(numbers)

    #listOfBlocked = numbers
        
    #print(img.shape)          

    r0, g0, b0 = 0, 0, 0
    r1, g1, b1 = 255, 255, 255

    def isQueen(mylist, numberofqueens):
        temp_height = []
        temp_width = []
        for i in range(0,height):
            temp_height.append((i/numberofqueens)*height)
        for i in range(0,width):
            temp_width.append((i/numberofqueens)*width)
        return (temp_height, temp_width)

    count = 0
    a, b = isQueen(listOfBlocked,50)
    for y in range(0,img.shape[0],10):
        for x in range(0,img.shape[1],10): #should be 13
            blocked = str(int(y / 10) +1)+','+str(int(x / 10) +1)
            #print(len(blocked))
            #print(blocked)
            if blocked in listOfBlocked:
                count+=1
                for i in range(10):
                    for j in range(10):
                        img[y+i][x+j][0] = r0
                        img[y+i][x+j][1] = g0
                        img[y+i][x+j][2] = b0
            else:
                for i in range(10):
                    for j in range(10):
                        img[y+i][x+j][0] = r1
                        img[y+i][x+j][1] = g1
                        img[y+i][x+j][2] = b1
    # Display the image
    print(count)
    # Save the image
    scipy.misc.imsave("./images/image"+str(number)+".png", img)
