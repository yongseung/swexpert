def find():

    dp = [ [ 0 for _ in range(K+1)] for _ in range(N+1)]
    
    for i in range(1,N+1):
        for j in range(1,K+1):
            if j<ITEM[i-1][0]:
                dp[i][j] = dp [i-1][j]
            else:
                dp[i][j]= max(dp[i-1][j], ITEM[i-1][1] + dp[i-1][j-ITEM[i-1][0]])1

    return dp[N][K]

for tc in range(1, int(input())+ 1):

    N, K = map(int, input().split())
    ITEM = [ list(map(int,input().split()))  for _ in range(N)  ]
    print("#{} {}".format(tc, find()))