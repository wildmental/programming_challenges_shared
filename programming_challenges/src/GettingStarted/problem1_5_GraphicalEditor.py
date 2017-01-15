outputField=[]
def IMN(M,N):
    """아웃풋 틀 잡기"""
    for i in range(0, N):
        outputField.append([])
        for j in range(0, M):
            outputField[i].append(0)

def C():
    for i in outputField:
        for j in outputField[i]:
            outputField[i][j]=0

def LXYC(X,Y,C):
    outputField[Y-1][X-1]=C

def VXYYC(X,Y1,Y2,C):
    for i in range(Y1-1, Y2):
        outputField[i][X-1]=C
        
def HXXYC(X1,X2,Y,C):
    for i in range(X1-1, X2):
        outputField[Y-1][i]=C

def KXYXYC(X1, Y1, X2, Y2, C):
    for i in range(X1-1, X2):
        for j in range(Y1-1, Y2):
            outputField[j][i]=C

def FXYC(X,Y,C):
    originC=outputField[Y-1][X-1]
    outputField[Y-1][X-1]=C
    for i in range(X-2,X+1):
        if i<0:
            continue
        elif i>len(outputField[1])-1:
            continue
        else:
            if outputField[Y-1][i]==originC:
                FXYC(i+1, Y, C)
    for j in range(Y-2,Y+1):
        if j<0:
            continue
        elif j>len(outputField)-1:
            continue
        else:
            if outputField[j][X-1]==originC:
                FXYC(X, j+1, C)    

def S(name):
    print(name)
    for i in outputField:
        for j in i:
            print(j,end="")
        print()

def menu():
    while 1:
        key=input("명령어를 입력하세요\n(입력예시-\nI M N\nC\nL X Y C\nV X Y Y C\nH X X Y C\nK X Y X Y C\nF X Y C\nS Name\nX)\n:")
        if key[0]=='I':
            k=key.split(" ")
            IMN(int(k[1]),int(k[2]))
        elif key[0]=='C':
            C()
        elif key[0]=='L':
            k=key.split(" ")
            LXYC(int(k[1]),int(k[2]),k[3])
        elif key[0]=='V':
            k=key.split(" ")
            VXYYC(int(k[1]),int(k[2]),int(k[3]),k[4])
        elif key[0]=='H':
            k=key.split(" ")
            HXXYC(int(k[1]),int(k[2]),int(k[3]),k[4])    
        elif key[0]=='K':
            k=key.split(" ")
            KXYXYC(int(k[1]),int(k[2]),int(k[3]),int(k[4]),k[5])
        elif key[0]=='F':
            k=key.split(" ")
            FXYC(int(k[1]),int(k[2]),k[3])
        elif key[0]=='S':
            S(key.split(sep=' ')[1]) 
        elif key[0]=='X':
            break
        else:
            print("명령어 오류")
            
menu()