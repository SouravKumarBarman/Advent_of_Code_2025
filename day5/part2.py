def sort_array(array_of_array:list[list[str]]):
    length=len(array_of_array)
    for i in range(length):
        for j in range(length-i-1):
            if(int(array_of_array[j][1])>int(array_of_array[j+1][1])):
                temp=array_of_array[j]
                array_of_array[j]=array_of_array[j+1]
                array_of_array[j+1]=temp
    return array_of_array

def stitch_range_together(array_of_array:list[list[str]]):
    length=len(array_of_array)
    i=int(0)
    while i<length-1:
        if int(array_of_array[i][0])>=int(array_of_array[i+1][0]) and int(array_of_array[i][1])<=int(array_of_array[i+1][1]):
            del array_of_array[i]
            if(i>0):
                i-=1
        elif int(array_of_array[i][1])>=int(array_of_array[i+1][0]):
            array_of_array[i][1]=array_of_array[i+1][1]
            del array_of_array[i+1]
        else:
            i=i+1
        length=len(array_of_array)
    return array_of_array

if __name__=='__main__':
    file=open("input.txt",'r')
    fresh_range=[]
    blank_line=int(0)
    count=0
    for line_number,line in enumerate(file):
        clean_line=line.strip()
        if clean_line=='' :
            blank_line=line_number
            break
        range_as_list=clean_line.split('-')
        fresh_range.append(range_as_list)
    sorted_fresh_range=sort_array(fresh_range)
    stitched_range=stitch_range_together(sorted_fresh_range)
    for final_range in stitched_range:
        count=count+int(final_range[1])-int(final_range[0])+1
    print(count)  