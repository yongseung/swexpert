
for tc in range(1, 11):
    N = int(input())
    t = [0] + [list(input().split()) for _ in range (N)]
    for i in range(len(t)-1,0,-1):
        if len(t[i]) == 4:
            if t[i][1] == "+":
                t[i] = [i, int(t[int(t[i][2])][1]) + int(t[int(t[i][3])][1])]
                
            elif t[i][1] == "-":
                t[i] = [i, int(t[int(t[i][2])][1]) - int(t[int(t[i][3])][1])]
               
            elif t[i][1] == "*":
                t[i] = [i, int(t[int(t[i][2])][1]) * int(t[int(t[i][3])][1])]         
            else:
                t[i] = [i, int(t[int(t[i][2])][1]) / int(t[int(t[i][3])][1])]

    print("#{} {}".format(tc, int(t[1][1])))