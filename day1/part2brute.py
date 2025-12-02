if __name__=="__main__":
    file=open("input.txt","r")
    index=int(50)
    count=0
    for line in file:
        line.strip()
        direction=line[0]
        num=int(line[1:])
        toAdd=0
        while(num>0): 
            num-=1
            if(direction=="R"):
                index+=1
                if index==100:
                    index=0
                if index==0:
                    count+=1
            else:
                index-=1
                if index==0:
                    count+=1
                if index==-1:
                    index=99
    print(count)