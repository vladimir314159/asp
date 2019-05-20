from makeLS import makeBoard, writeToFile
import math

for sizeBoard in range(5,100):
    for numberBlocked in range(1,math.floor((sizeBoard*sizeBoard)/3)):
        board, numbers = makeBoard(sizeBoard,numberBlocked)
        writeToFile(board,numbers,sizeBoard)