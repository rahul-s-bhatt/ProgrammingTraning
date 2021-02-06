import sys

range = xrange
input = raw_input

N = int(input())

arr = list(map(int, input().split()))

arr = sorted(arr)

summ = 0
res = 0

for i in range(N):
	if summ == 1:
		summ = 0
		continue

	else:
		summ = (arr[i] % 2)
		res += (arr[i] // 2)
print res