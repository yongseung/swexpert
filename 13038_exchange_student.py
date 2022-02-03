def find_weeks(s):
    if T % s == 0: 
        day = int((T-1)/s)*7 
        remain = s
    else:
        day = int(T/s)*7 
        remain = T%s
    return day, remain

def find_day(remain, start):
    min_day = 7
    for i in range(len(start)):
        find_class = 0
        temp_day = 0
        for j in range(start[i],len(TEMP)):
            temp_day += 1
            if TEMP[j] == 1:
                find_class += 1
            if find_class == remain:
                if temp_day < min_day:
                    min_day = temp_day
                break
    return min_day

for tc in range(1, int(input())+ 1):
    T = int(input())
    TABLE = list(map(int,input().split()))
    start = [i for i, val in enumerate(TABLE) if val == 1]
    cnt_per_week = len(start)
    TEMP = TABLE*2
    day, remain = find_weeks(len(start))
    print("#{} {}".format(tc,day + find_day(remain, start)))