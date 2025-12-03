import re

def find_id_in_range(start:int, end:int):
    sum=int(0)
    for Id in range(start, end+1):
        result=re.match(r'^(\d+)\1$',str(Id))
        if result:
            print(result.string)
            sum+=int(result.string)
    return sum

if __name__=='__main__':
    file=open("input.txt",'r')
    input = file.readline()
    list_input=input.split(',')
    array_of_array=[]
    output=int(0)
    for element in list_input:
        temp=element.split('-')
        array_of_array.append(temp)
    for array in array_of_array:
        output+=find_id_in_range(int(array[0]),int(array[1]))
    print(output)
        