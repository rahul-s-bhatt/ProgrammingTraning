import math

def solve(n, k, arr):
	if k%(k-1) == 0:
		return "YES"
	else:
		for i in arr:
			if math.gcd(i,k)==1:
				return "NO"
				break
	return "YES"


for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))

	print(solve(n, k, arr))