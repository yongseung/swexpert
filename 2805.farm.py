def farm():
 
    t= sum(matrix[int(len(matrix)/2)])
    for i in range(int(len(matrix)/2)):
        for up in range(int(len(matrix)/2) -i, int(len(matrix)/2)+1+i, 1):            
            t += matrix[i][up]
            t +=matrix[-i -1][up]
    return t
 
for tc in range(1, int(input()) + 1):
    size=int(input())
    matrix= [ [ int(i) for i in str(input()) ] for _ in range(size)]
    print("#{} {}".format(tc, farm()))