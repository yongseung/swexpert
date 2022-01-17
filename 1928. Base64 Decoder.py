table =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
T = int(input())
for i in range(1, T+1):
    b = str(input()) #20
    decode_table=[]
    result = []
    
    for j in range(len(b)):
        index=0
        for find_index in range(len(table)):
            if b[j] == table[find_index]:
                index=find_index
                break
                 
        decode_table.append(index)
         
    for j in range(0, len(decode_table), 4):
        store = [0 for i in range(4)]
        for k in range(4):
            if k == 0:
                store[k]=(decode_table[j+k]<<k+2)
            else:
                store[k-1]= (store[k-1] + (decode_table[j+k] >> (3-k)*2 ))
                store[k]=(decode_table[j+k]<<2*(k+1))% 512 % 256
                 
        for l in range(3):
            result.append(chr(store[l]))
             
    s=''.join(result)
    print("#{} {}".format(i, s))