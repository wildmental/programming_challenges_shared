'''
Created on 2017. 1. 1.

@author: BJ Park
'''

inputField=[]
outputField=[]

def inputSize(ab):
    return ab.split(" ")
    
def inputLine(M,N):
    for i in range(0,M):
        line=input(str(i+1)+"번째 행 입력(길이 "+str(N)+"의 문자열)\n예시 - '*...'\n")
        fields=[line[i] for i in range(0,len(line))]
        inputField.append(fields)
    else:
        for i in range(0,M):
            for j in range(0,N):
                print(inputField[i][j],end="")
            print()

def output(M,N):
    """아웃풋 틀 잡기"""
    for i in range(0, M):
        outputField.append([])
        for j in range(0, N):
            outputField[i].append(0)
    
    """아웃풋 값 입력"""
    for i in range(0, M):
        for j in range(0, N):
            if inputField[i][j] == "*":
                """지뢰입력"""
                outputField[i][j]="*"
                """주변 값 입력"""
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        if k==i and l==j:
                            continue
                        elif k<0 or l<0:
                            continue
                        elif k>M-1 or l>N-1:
                            continue
                        elif outputField[k][l] =="*":
                            continue 
                        outputField[k][l]+=1
    for i in outputField:
        for j in i:
            print(j,end="")
        print()
        
def main():
    M,N=inputSize(input("영역 사이즈 입력 : 예시 - 'M N'(M이 행, N이 열)\n"))
    M=int(M)
    N=int(N)
    inputLine(M,N)
    output(M, N)
        
main()
for i in inputField:
    print(i)
for i in outputField:
    print(i)