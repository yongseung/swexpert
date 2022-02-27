def find_destination():
    row,col = 0,0
    for i in range(100):
        for j in range(100):
            if matrix[i][j] == 2:
                row=i
                col=j
                return (row,col)
    return (row,col)

def find_x(matrix):
    now_row, now_col = find_destination()
    dCol = [-1, 1,0]
    dRow = [0,0,-1]
    move = 0
    while True:
        if now_col + dCol[move] < 0 or now_col + dCol[move] > 99:
            move += 1
        elif matrix[now_row + dRow[move]][now_col + dCol[move]] == 1:
            matrix[now_row + dRow[move]][now_col + dCol[move]] = 2
            now_row = now_row + dRow[move]
            now_col = now_col + dCol[move]
            move = 0
        else:
            move += 1
        if now_row == 0:
            return now_col

    return now_col

for tc in range(1, 11):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    print("#{} {}".format(tc,find_x(matrix)))