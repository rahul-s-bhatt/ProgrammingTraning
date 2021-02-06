import sys

range = xrange
input = raw_input

for _ in range(int(input())):
	n = int(input())

	arr = list(map(int, input().split()))
	res = 0
	minElem = sys.maxsize
	for i in arr:
		minElem = min(i, minElem)
		res += minElem
	print res