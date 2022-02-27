
def find_min():
    global INF
    temp_min = INF
    for i in range(N):
        if G[i][i] < temp_min:
            temp_min = G[i][i]
        for j in range(i+1,N):
            if G[i][j] + G[j][i] < temp_min:
                #print("G {} i {} j {}".format(G[i][j], i, j))
                temp_min = G[i][j]+G[j][i]
    return temp_min

for tc in range(1, int(input()) + 1):
    INF=99999
    N, M = map(int,input().split())
    G = [[INF for _ in range(N)] for i in range(N)]
    #ignore self circle
    for i in range(M):
        s,e,c = map(int,input().split())
        #print("{} {} {}".format(s,e,c))
        #if s != e:
            #print("s is not same with e{} {} ".format (s,e))
        G[s-1][e-1] = c

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if G[i][k] + G[k][j] < G[i][j]:
                    G[i][j] = G[i][k] + G[k][j]
    #print(G)
    print("#{} {}".format(tc,find_min()))





