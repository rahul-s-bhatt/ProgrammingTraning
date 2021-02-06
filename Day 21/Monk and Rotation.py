
"""
https://www.hackerearth.com/practice/codemonk/
"""

t = int(input())

for i in range(t):
    n, k = input().split()
    n = int(n)
    k = int(k)

    arr = list(map(int, input().split()))
    temp = []
    
    for j in range(n):
        d = ((j + (n - k)) % n)
        temp.append(arr[d])
    
    print(*temp)