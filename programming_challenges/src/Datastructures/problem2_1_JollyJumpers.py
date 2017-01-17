print(":::::Start JollyJumpers!:::::")

lines=[]
line=[]
def getLine():
    lines=[]
    while True:
        line=input("input a sequence of numbers :").strip().split(sep=" ")
        print(line)
        if line==['']:
            break
        lines.append(line)
        print(lines)

jolly=[]checker=[]
def judge():
    for line in lines:
        for i in range(1,len(line)):
            checker.append(i)
            gap=(int(line[i])-int(line[i-1]))>0and(int(line[i])-int(line[i-1]))or-(int(line[i])-int(line[i-1]))
            jolly.append(gap)
        if sorted(jolly)==checker:
            print("jolly")
        else:
            print("not jolly")    
    else:
        lines=[]
        line=[]
        print("done")
                
while 1:
    getLine()
    print(lines)
    judge()