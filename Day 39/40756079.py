# cook your dish here
t = int(input())

for i in range(t):
     n,k = map(int,input().split())
     arr = [ int(x) for x in input().split()]
     freq = [0]*(k+1)
     max_count = 0
     start_index = 0
     end_index = 0

     hash_count = 0
     while(end_index<n):
         freq[arr[end_index]] = freq[arr[end_index]] + 1
         if(freq[arr[end_index]] == 1):
             hash_count = hash_count + 1
         while(hash_count>=k):
             freq[arr[start_index]] = freq[arr[start_index]] - 1
             if(freq[arr[start_index]]==0):
                hash_count = hash_count-1
             start_index = start_index + 1
         max_count = max(max_count,end_index-start_index+1)
         end_index = end_index + 1

     print(max_count)




