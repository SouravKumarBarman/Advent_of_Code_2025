if __name__=='__main__':
    file=open("input.txt",'r')
    fresh_range=[]
    blank_line=int(0)
    count=int(0)
    for line_number,line in enumerate(file):
        clean_line=line.strip()
        if clean_line=='' :
            blank_line=line_number
            break
        range_as_list=clean_line.split('-')
        fresh_range.append(range_as_list)
    file=open("input.txt",'r')
    for line_number,line in enumerate(file):
        if(line_number>blank_line):
            clean_line=line.strip()
            for id_range in fresh_range:
                if int(clean_line)>=int(id_range[0]) and int(clean_line)<=int(id_range[1]):
                    count+=1
                    break
    print(count)