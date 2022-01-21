def pruning(col):
    for i in range(col):
        if BOARD[col] == BOARD[i] or abs(BOARD[col] - BOARD[i]) == int(col-i):
            return False
    return True
     
def nqueen(n):
    global CNT
    if n  == SIZE:
        CNT = CNT +1
        return True
        
    for i in range(SIZE):
        BOARD[n] = i
        if pruning(n):
            nqueen(n+1)        
    return True
 
for tc in range(1, int(input()) + 1):
    global BOARD
    global SIZE
    global CNT
    CNT = 0
    SIZE = int(input())
    BOARD = [ 0 for _ in range(SIZE) ]
    nqueen(0)
    print("#{} {}".format(tc, CNT))