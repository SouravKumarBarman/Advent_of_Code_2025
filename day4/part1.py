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
    i_rows, i_cols = len(image), len(image[0])
    k_rows, k_cols = len(kernel), len(kernel[0])
    total_sum=int(0)
    # 1. Slide the window vertically
    for y in range(i_rows-k_rows+1):
        # 2. Slide the window horizontally
        for x in range(i_cols-k_cols+1):
            
            # 3. Perform the "Multiply and Sum" (Element-wise)
            segment_sum = 0
            for i in range(k_rows):
                for j in range(k_cols):
                    if(image[y + 1][x + 1]==1):
                        segment_sum += image[y + i][x + j] * kernel[i][j]
                    else:
                        segment_sum=-1
            if segment_sum<4 and segment_sum>-1:
                total_sum+=1
    return total_sum


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