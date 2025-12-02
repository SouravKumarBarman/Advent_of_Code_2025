def move_right(index: int,num:int):
    temp=int(0)
    if index==0:
        temp=num//100
    elif num>=(100-index):
        temp=((num-(100-index))//100)+1
    return (index+num)%100, temp


def move_left(index:int, num:int):
    temp=int(0)
    if index==0:
        temp=num//100
    elif(num>=index):
        temp=((num-index)//100)+1
    return (index-num)%100, temp
    

if __name__=="__main__":
    file=open("input.txt","r")
    index=int(50)
    count=0
    for line in file:
        line.strip()
        direction=line[0]
        num=int(line[1:])
        toAdd=0
        if(direction=="R"):
            index,toAdd=move_right(index,num)
        else:
            index,toAdd=move_left(index, num)
        count+=toAdd
    print(count)