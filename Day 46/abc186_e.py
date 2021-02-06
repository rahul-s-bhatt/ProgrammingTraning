import math

for _ in range(int(input())):
	n, s, k = map(int, input().split())

	if math.gcd(n, k) != 1:
		print(-1)
	else:
		d = math.gcd(n, s, k)
