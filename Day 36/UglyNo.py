# ugly no are those whose prime facts are 2, 3 or 5.

n = int(input())

# prime factors (2, 3, 5) only of number n

# divide no by 2 until it cannot be further divided

lookup = {}

def oneForAll(n):
	while n % 2 == 0:
		n = n / 2

	while n % 3 == 0:
		n = n / 3

	while n % 5 == 0:
		n = n / 5

	return 1 if n==1 else 0

i = 1
uglyNoCount = 1

while n > uglyNoCount:
	i += 1
	if i in lookup:
		print lookup[i]
	if oneForAll(i):
		uglyNoCount += 1
		lookup[i] = uglyNoCount

print i
print lookup