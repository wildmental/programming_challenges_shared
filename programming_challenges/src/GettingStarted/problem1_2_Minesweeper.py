'''
Created on 2017. 1. 1.

@author: BJ Park
'''
from msilib import Table


    
def inputField(j):
    lines=j.split(sep="\n")
    field = Table.__init__()
    col=0
    row=0
    for line in lines:
        i=line.split()
        for k in i:
            field.add_field(k, [row,col], str)
            col+=1
        else : row+=1
    return field

def output():
    a=input("필드 사이즈 입력(예시 - M N) : ")
    M,N = a.split(sep=" ")
    M=int(M)
    N=int(N) 
    field=inputField(input("필드내용 입력 :\n (예시 - \n *...\n ...*)\n"))
    row=0
    col=0
    while row<=M and col<=N:
        field[row,col]