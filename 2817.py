def find(idx, sum):
    global CNT
    if idx == len(m):
        return

    temp = sum + m[idx]
    if temp == K:
        CNT +=1
        find(idx+1, sum)
    else:
    	find(idx+1, sum)
    	find(idx+1, temp) 

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    m = [ int(i) for i in input().split() ]
    CNT = 0
    find(0,0)

    print("#{} {}".format(tc,CNT))