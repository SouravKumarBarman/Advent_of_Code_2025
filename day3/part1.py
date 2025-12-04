def find_greatest_digits(input : str):
    length=len(input)-1
    msb=int(input[length-1])
    lsb=int(input[length])
    length-=1
    while(length>0):
        length-=1
        if int(input[length])>=msb:
            if(msb>lsb):
                lsb=msb
            msb=int(input[length])
    print((10*msb)+lsb)
    return (10*msb)+lsb


if __name__=='__main__':
    file=open("input.txt",'r')
    output=int(0)
    for line in file:
        clean_line=line.strip()
        print(clean_line,end='->')
        output+=find_greatest_digits(clean_line)
    print(output)
