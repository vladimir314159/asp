import random
import copy
def removePosible(board,sizen,x,y,n):
    for i in range(0,sizen):
        if n in board[x-1][i]:
            board[x-1][i].remove(n)
    for j in range(0,sizen):
        if n in board[j][y-1]: 
            board[j][y-1].remove(n)
    
def makeBoard(sizeofn,numberInit):
    setInts = set([])
    xInts = []
    for i in range(1,sizeofn+1):
        setInts.add(i)
    for i in range(1,sizeofn+1):
        xInts.append(copy.deepcopy(setInts))
    # initualizes the ints
    board = []
    for i in range(1,sizeofn+1):
        board.append(copy.deepcopy(xInts))
    # initualizes the board
    listOfUsed = []
    numbers = []
    x = random.randint(1,sizeofn)
    y = random.randint(1,sizeofn)
    number = random.sample(board[x-1][y-1],1)
    numbers.append(number[0])
    print(number)
    listOfUsed.append((x,y))
    removePosible(board,sizeofn,x,y,number[0])
    while len(listOfUsed) != numberInit:
        x = random.randint(1,sizeofn)
        y = random.randint(1,sizeofn)
        number = random.sample(board[x-1][y-1],1)
        if (x,y) in listOfUsed:
            continue
        numbers.append(number[0])
        removePosible(board,sizeofn,x,y,number[0])
        listOfUsed.append((x,y))
    print("listOfUsed:",listOfUsed)
    print("board:",board)
    print("numbers",numbers)
    return listOfUsed, numbers

def writeToFile(board,numbers,n):
    f = open("./LS/LS"+"n="+str(n)+"blocked="+str(len(numbers))+".lp","w")
    f.write("#const n= "+str(n)+".\n")
    for i in range(0,len(numbers)-1):
        print(i)
        f.write("q("+str(board[i][0])+","+str(board[i][1])+","+str(numbers[i])+").\n")
    #while len(listOfUsed) != sizeofn:
board, numbers = makeBoard(100,4000)
writeToFile(board,numbers,100)