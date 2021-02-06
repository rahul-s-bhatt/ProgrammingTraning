# no. of subsets of a set having sum gt_eq than a val
import math

def solve(a, n, k):
	count = 0

	for i in range(0, int(math.pow(2, n))):
		target = 0

		for j in range(n):
			if j|(1<<i):
				target += a[j]
				print(a[j])

		if target >= k:
			count += 1
	return count

a = [1, 2, 3, 4, 5]
n = 5
k = 12

print(solve(a, n, k))