n, m, t = map(int, input().split())

for i in range(m+1):
	a, b = map(int, input().split())

	if i > a and i <= b and n:
		n += 1
	else:
		n -= 1

if n <= 0:
	print()