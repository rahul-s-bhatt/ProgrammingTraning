from bisect import bisect_right
n = int(input())
k = []
ans = 0

arr = list(map(int,input().split()))

for i in arr:
    x = bisect_right(k,i)
    ans += len(k)-x
    k.insert(x,i)
print(ans)