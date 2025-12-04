def find_greatest_in_range(string:str,start:int, end:int):
    num=int(string[end])
    index=end
    while end>start:
        end-=1
        if(int(string[end])>=num):
            num=int(string[end])
            index=end
    return num,index+1

def find_12_greatest_digits(input : str):
    length=len(input)
    my_list=[]
    index=int(0)
    for i in range(0,12):
        toAdd,index=find_greatest_in_range(input,index,length-(12-i))
        my_list.append(str(toAdd))
    result_string="".join(my_list)
    print(result_string)
    return int(result_string)
    


if __name__=='__main__':
    file=open("input.txt",'r')
    output=int(0)
    for line in file:
        clean_line=line.strip()
        output+=find_12_greatest_digits(clean_line)
    print(output)
