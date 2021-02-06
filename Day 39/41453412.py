# cook your dish here
try:
  
    for _ in range(int(input())):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
    
        h = dict([(i,0) for i in range(1,k+1)])
        j = max_length = types = cur_max = 0
        k -= 1
        for i in range(n):
            h[a[i]] += 1
            if h[a[i]]==1: types+=1
            while types > k:
                h[a[j]]-=1
                if h[a[j]]==0: types-=1
                j +=1
            max_length = max(max_length, i-j+1)
        print(max_length)
                
            
    
            
            
    
    
    
        
    
    
        
except EOFError:
    pass
