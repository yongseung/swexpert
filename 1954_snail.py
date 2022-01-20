T = int(input())
for test_case in range(1, T + 1):
    matrix_size = int(input())
    array = [[0 for col in range(matrix_size)] for row in range(matrix_size)]
    cnt = 1
    now_r=0
    now_c=0
 
    for circular in range(1,int((matrix_size-1)/2)+2):
        #Right()
        for right_row in range(circular-1,matrix_size-circular+1):
            array[now_c][right_row] = cnt
            cnt+=1
        now_r=matrix_size-circular
        if cnt == matrix_size*matrix_size:
            break; 
        #Down()
        for down_col in range(now_c+1,matrix_size-circular+1):
            array[down_col][now_r]=cnt
            cnt+=1
        now_c=matrix_size-circular
          
        #Left()
        for left_row in range(now_r-1,circular-2, -1):
            array[now_c][left_row] = cnt
            cnt+=1
        now_r=circular-1
         
        if cnt == matrix_size*matrix_size:
            break;
        #Up
        for up_col in range(now_c-1,circular-1 , -1):
            array[up_col][now_r] = cnt
            cnt+=1
        now_c=circular
     
    print("#{}".format(test_case))
    for col in range(matrix_size):
        for row in range(matrix_size):
            print(str(array[col][row]), end =' ')
        print()