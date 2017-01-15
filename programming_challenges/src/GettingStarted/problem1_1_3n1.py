'''
Created on 2016. 12. 31.

@author: BJ Park
'''

def alg1(k):
    count=[]
    a=int(k[0])
    b=int(k[1])
    if a<b : 
        i=a
        j=b
    else : 
        i=b
        j=a
    while i!=j+1:
        count.append(alg2(i))
        i+=1
    else: return ""+str(a)+" "+str(b)+" "+str(max(count))

def alg2(n):
    count=1
    while n!=1 :
        if n%2 ==0:
            n//=2
            count+=1
        elif n%2 ==1:
            n=(n*3+1)//2
            count+=2
    else:
        return(count)

def integrate():
    results=[]
    while len(results) < 10 :
        results.append(alg1(k=input("입력 예시 : i j\n").split(sep=" ")))
    else : 
        for i in results: 
            print(i)

integrate()