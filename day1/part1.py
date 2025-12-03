def move_right(index: int,num:int):
    return (index+num)%100


def move_left(index:int, num:int):
    return (index-num)%100
    

if __name__=="__main__":
    file=open("input.txt","r")
    index=int(50)
    count=0
    for line in file:
        direction=line[0]
        num=int(line[1:])
        if(direction=="R"):
            index=move_right(index,num)
        else:
            index=move_left(index, num)
        if(index==0):
            count=count+1
    print(count)