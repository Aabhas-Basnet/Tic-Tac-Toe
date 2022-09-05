List=[["_","_","_"],
   ["_","_","_"],
   ["_","_","_"]]

n = 0

def Display():
    for i in range(3):
        s=" "
        for j in range(3):
            s=s+str(List[i][j])+" "
        print(s)

def Checkturn():
    while(True):
            turn = input("Enter your turn 1 or 2: ")
            if turn == '1' or turn == '2':
                Display()
                break
            else:
                print("Chose either 1 or 2 only")
    return(turn)

def getInputrow():
    while(True):
        row = int(input("Enter the row number: "))

        if (row>3 or row<0):
            print("Invalid")
        else:
            break
    return(row)

def getInputcol():
    while(True):
        col = int(input("Enter the column number: "))

        if (col>3 or col<0):
            print("Invalid")
        else:
            break
    return(col)
    

    col = int(input("Enter the column number: "))
def userInput():
    while(True):
        row = getInputrow()
        col = getInputcol()

        if List[row-1][col-1] == 'X' or List[row-1][col-1] == "O":
            print("This position is already chosen! Try empty position: ")
        else:
            if n%2 == 0:
                List[row-1][col-1] = "X"
            else:
                List[row-1][col-1] = "O"
            break

    return(List)

def computerInput():
    import random
    while(True):
        row1 = random.randint(0,2)
        col1 = random.randint(0,2)

        if List[row1][col1] == '_':
            if turn == '1':
                List[row1][col1]="O"
            else:
                List[row1][col1]="X"
            break
    print("Computer Chosed the position: ",row1+1,", ",col1+1)
    return(List)

turn = Checkturn()
P1 = 0
P2 = 0

while(n<9):
    if turn == '1':
        if n%2 == 0:
            userInput()
        else:
            computerInput()
    if turn == '2':
        if n%2 !=0:
            userInput()
        else:
            computerInput()
    n=n+1
    Display()

    for i in range(3):
        N1 = N2 = T1 = T2 = D1 = D2 = D3 = D4 = 0
        for j in range(3):
            if List[i][j] =="X":
                N1 = N1+1
            elif List [i][j] =="O":
                N2= N2+1

            if List[j][i] =="X":
                T1 = T1+1
            elif List [j][i] =="O":
                T2= T2+1

            if List[0][0] == List[1][1] == List[2][2] == "X":
                D1=D1+1
            elif List[0][0] == List[1][1] == List[2][2] == "O":
                D2=D2+1

            if List[0][2] == List[1][1] == List[2][0] == "X":
                D3=D3+1
            elif List[0][2] == List[1][1] == List[2][0] == "O":
                D4=D4+1
                
            if N1 ==3 or T1 == 3 or D1 == 1 or D3 == 1:
                P1 = 1

            if N2 ==3 or T2 == 3 or D3 == 1 or D4 == 1:
                P2 = 1
               
    if P1 == 1 or P2 == 1:
        break


if P1==1:
    print("Congratulations You win")
elif P2 == 1:
    print("Computer wins")
else:
    print("Draw")
