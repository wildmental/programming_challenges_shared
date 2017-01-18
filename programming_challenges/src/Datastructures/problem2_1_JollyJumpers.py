print(":::::Start JollyJumpers!:::::")

def getLine():
    line=[]
    lines=[]
    while True:
        line=input("input a sequence of numbers :").strip().split(sep=" ")
        #print(line)
        if line==['']:
            return lines
        lines.append(line)
        #print(lines)

def judge(lines):
    for line in lines:
        jolly=[]
        checker=[]
        for i in range(1,len(line)):
            checker.append(i)
            gap=(int(line[i])-int(line[i-1]))>0 and (int(line[i])-int(line[i-1]))or-(int(line[i])-int(line[i-1]))
            jolly.append(gap)
        if sorted(jolly)==checker:
            #print(checker, jolly)
            print("jolly")
        else:
            #print(checker, jolly)
            print("not jolly")
    else:
        lines=[]
        line=[]
        print("done")

while 1:
    lines=getLine()
    #print(lines)
    judge(lines)
