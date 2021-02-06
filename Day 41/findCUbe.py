n = int(input())

arr = list(map(int, input().split()))
c = 0
for i in arr:
	if round(i**(1/3)) ** 3 == i:
		c += 1

print(c)