#1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기 D2
t2 = int(input())
def f(m):
    t = [0 for i in range(101)]
    fm = 0
    fi = 0
    for i in m:
        t[i]+=1
    for i in range(101):
        if fm <= t[i]:
            fm = t[i]
            fi = i
    return fi   
 
for i in range(t2):
    j=input()
    ml = list(map(int, input().split()))
    print("#{} {}".format(j, f(ml)))