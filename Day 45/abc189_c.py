N = int(input())

arr = list(map(int, input().split()))

ans = 0

for l in range(N):
	mn = arr[l]
	for r in range(l, N):
		mn = min(mn, arr[r])
		ans = max(ans, (r-l+1)*mn)

print(ans)