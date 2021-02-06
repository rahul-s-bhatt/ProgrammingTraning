n, k = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(n):
	for j in range(i+1, n):
		if arr[i]+arr[j] == k:
			print(i, j)
			break