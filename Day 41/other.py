n, k = map(str, input().split())

c = 0

for i in n:
	if i != k:
		c += 1
print(c)