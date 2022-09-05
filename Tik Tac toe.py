List=[["_","_","_"],
   ["_","_","_"],
   ["_","_","_"]]

P1 = 0
P2 = 0
n = 0

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

while(n<9):
    
    row = getInputrow()
    col = getInputcol()

    if List[row-1][col-1] == 'X' or List[row-1][col-1] == "O":
        print("This position is already chosen! Try empty position: ")
    else:
        if n%2 == 0:
            List[row-1][col-1] = "X"
        else:
            List[row-1][col-1] = "O"

        n=n+1

    for i in range(3):
        s=" "
        for j in range (3):
            s = s+str(List[i][j])+" "
        print(s)

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
    print("Player 1 WINS")
elif P2 == 1:
    print("Player 2 WINS")
else:
    print("Draw")
