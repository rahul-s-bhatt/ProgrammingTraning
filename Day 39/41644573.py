# cook your dish here
T = int(input())
for t in range(T):
    [N, K] = [int(x) for x in input().strip().split()]
    array = [int(x) for x in input().strip().split()]
    start = 0
    end = 0
    unique_count = 0
    freq = {}
    for val in range(K):
        freq[val+1] = 0
    max_len = 0
    
    for end in range(N):
        val = array[end]
        if freq[val]==0:
            unique_count += 1
        freq[val] +=1
        
        
        while unique_count>=K:
            
            
            # remove element at start
            to_remove = array[start]
            while array[start]==to_remove:
                start+=1
                freq[to_remove] -=1

            if freq[to_remove]==0: unique_count -= 1 
            
        length = end-start+1
        if length>max_len: max_len=length
    if max_len==0: max_len=N 
    print(max_len)