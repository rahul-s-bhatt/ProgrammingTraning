N = int(input())

arr = list(map(int, input().split()))

n = 1<<N

max1 = max(arr[:(1<<N-1)])
max2 = max(arr[(1<<N-1):])

if max1>max2:
	print(arr.index(max2)+1)
else:
	print(arr.index(max1)+1)