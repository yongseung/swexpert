def combination(idx, arr, last):
    #print("start idex = {} arr = {} last {}".format(idx,arr, last))
    if idx == 3:
        return result.append(arr)
        
    for i in range(idx + last, L):
        combination(idx+1,[M[i]]+arr, last)
        #print("after idex = {} arr = {} last {}".format(idx,arr, last))
        last += 1

def get_fifth():
    temp = []
    for i in range(len(result)):
        temp.append(sum(result[i]))

    del_dup = list(set(temp))
    del_dup.sort(reverse=True)
    return del_dup[4]

for tc in range(1, int(input()) + 1):
    M = list(map(int, input().split()))
    L = len(M)
    result = []
    combination(0,[],0)
    print("#{} {}".format(tc,get_fifth()))