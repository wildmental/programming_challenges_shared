'''
Created on 2017. 1. 10.

@author: BJ Park
'''
candyNames=[]
VoteMatrix=[]
candyGet=[]
result=[]

def getCaseNum():
    return input("투표횟수 입력")

def getCandyNum():
    return input("후보 수 입력")

def getBallotNum():
    return input("유권자 수 입력") 

def getCandyName(name):
    candyNames.append(name)
    candyGet.append(0)

def getVote(vote):
    VoteMatrix.append(vote.split(" "))
    
def allIndex(x, list_):
    indexes=[]
    for i in list_:
        if i == x:
            indexes.append(list_.index(x))
    return indexes

def remain(list_):
    posiList=list_
    for i in posiList:
        if i<0:
            posiList.remove(i)
    return posiList

def minVote(list_):
    posiList=list_
    for i in posiList:
        if i<0:
            posiList.remove(i)
    return min(posiList)
    
def count(m,b):
    reps=0
    #숫자세기
    for i in m:
        candyGet[int(i[reps])-1]+=1
    while max(candyGet)<=b//2:
        for j in allIndex(minVote(candyGet), candyGet):    
            for k in m:
                if int(k[reps])-1==j:
                    candyGet[int(k[reps+1])-1]+=1
            candyGet[j]=-1
        if max(remain(candyGet))==min(remain(candyGet)):
            names=[]
            for idx in allIndex(max(remain(candyGet)),candyGet):
                names.append(candyNames[idx])
            return names
    else:
        return candyNames[candyGet.index(max(candyGet))]
        
def main():
    cases = int(getCaseNum())
    print()
    for x in range(cases):
        print(x)
        #후보자 수를 입력받고 그 횟수만큼 후보자 이름 배열에 append
        candyNum=int(getCandyNum())
        for i in range(candyNum):
            getCandyName(input(str(i+1)+"번째 후보 이름 입력:"))
        #유권자 수를 입력받고 그 횟수만큼 투표 실시
        ballotNum=int(getBallotNum())
        for j in range(ballotNum):
            getVote(input(str(j+1)+"번째 유권자 투표 실시:"))
        #반복 카운트 및 결과도출
        print(count(VoteMatrix,ballotNum))
        
main()