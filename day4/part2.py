def pad_matrix(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    left_pad = [0]
    right_pad = [0]
    # 3. Pad the existing rows (Left + Row + Right)
    padded_rows = []
    for row in matrix:
        padded_rows.append(left_pad + row + right_pad)
    # 4. Create Top and Bottom padding rows
    full_width = cols + 2
    top_bottom_row = [0] * full_width
    # 5. Stack everything together: Top Pads + Middle + Bottom Pads
    final_matrix = []
    final_matrix.append(list(top_bottom_row)) 
    final_matrix.extend(padded_rows)
    final_matrix.append(list(top_bottom_row))
    return final_matrix

def convolve_2d(image, kernel):
    x=len(image)-2
    y=len(image[0])-2

    i=len(kernel)
    j=len(kernel[0])
    count=0
    array_of_X=[]
    while True:
        array_of_X=[]
        for a in range(x):
            for b in range(y):
                kernel_sum=0
                for c in range(i):
                    for d in range(j):
                        if(image[a+1][b+1]==1):
                            kernel_sum+=image[a+c][b+d]*kernel[c][d]
                        else:
                            kernel_sum=-1
                if kernel_sum<4 and kernel_sum>-1:
                    count+=1
                    array_of_X.append([a+1,b+1])
        if(len(array_of_X)!=0):
            for point in array_of_X:
                image[point[0]][point[1]]=0
        else:
            break
    return count

if __name__=='__main__':
    file=open("input.txt",'r')
    matrix=[]
    for line in file:
        clean_line=line.strip()
        clean_line=clean_line.replace('@','1')
        clean_line=clean_line.replace('.','0')
        int_list=[]
        for character in clean_line:
            int_list.append(int(character))
        matrix.append(int_list)

    matrix=pad_matrix(matrix)
    kernel=[[1,1,1],
            [1,0,1],
            [1,1,1]]
    output=convolve_2d(matrix,kernel)
    print(output)