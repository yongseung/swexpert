N_SET = []
MAX_SET = []
    
    
def search(n,current_index, now, repeat, c_max):
    global IS_RESULT_MAX
    if now == repeat:
        temp_max = 0
        for i in range(len(n)):
            temp_max = temp_max + n[i] * (10**(len(n)-i-1))

        if IS_RESULT_MAX < temp_max:
            IS_RESULT_MAX = temp_max       
        return True
    
    elif MAX_SET == n: # final 
        if len(N_SET) !=len(n): # and has same value total finish
            search(n,current_index,repeat, repeat, c_max)
        else: 
            if int(repeat - now) % 2 == 0: # even cnt exchange again
                search(n,current_index, repeat, repeat, c_max)
            else:
                n[-1], n[-2] = n[-2], n[-1] # odd, finish
                search(n,current_index, repeat, repeat, c_max)
                
    else: # max not, finish 
        c_max_set_index =[ int(i)   for i in range(current_index+1, len(n)) if c_max == n[i] ]
        if n[current_index] < c_max:
            for i in c_max_set_index:
                new_n = list(n)
                new_n[current_index] , new_n[i]  = new_n[i], new_n[current_index]
                c_max = max(new_n[current_index+1:])
                search(new_n,current_index+1,now+1,repeat, c_max)
        else:
            search(n,current_index+1,now,repeat, c_max)

            # for i in range(now+1, len(n)):
            #     c_max = max(n[i:])
            #     c_max_set_index = [ j for j in range(i, len(n)) if c_max == n[j] ]
            #     if n[i] < c_max: 
            #         for j in c_max_set_index:
            #             new_n = list(n)
            #             new_n[i] , new_n[j]  = new_n[j], new_n[i]
            #             c_max = max(new_n[i+1:])
            #             search(new_n,now+1,repeat, c_max)
    return True
    
    
for tc in range(1, int(input()) + 1):
    line, repeat = map(int, input().split())
    line = str(line)
    numbers = [ int(line[i]) for i in range (len(line))]

    MAX_SET= sorted((numbers), reverse=True)
    global IS_RESULT_MAX
    IS_RESULT_MAX = 0

    N_SET = sorted(set(numbers), reverse=True)

    search(numbers, 0, 0, repeat, N_SET[0])
    print("#{} {}".format(tc, IS_RESULT_MAX))