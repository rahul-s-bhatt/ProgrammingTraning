import sys, math
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)

def I(): return int(sys.stdin.readline().rstrip())
def MI():return map(int, sys.stdin.readline().rstrip().split())
def LI():return list(map(int, sys.stdin.readline().rstrip().split()))
def LI2():return list(map(int, sys.stdin.readline().rstrip()))
def S():return sys.stdin.readline().rstrip()
def LS():return list(sys.stdin.readline().rstrip().split())
def LS2():return list(sys.stdin.readline().rstrip())

for i in range(I()):
	n = I()
	W = LI()
	L = LI()

	pos = [i for i in range(n)]

	hits = 0

	i, j = 0, 1
	while i < n-1:
		j = i+1
		while j < n:
			if W[i] > W[j]:
				pos[i] += L[i]
				hits += 1
			j += 1
		i = bisect_left(pos, pos[i])-1
		# i += 1
	print(pos, hits)
	# i, j = 0, 1
	# while i < n-1:
	# 	j = i+1
	# 	while j < n:
	# 		if pos[i] <= pos[j] and W[i] > W[j]:
	# 			# if W[i] < W[j]:
	# 			# 	continue	
	# 			# else:
	# 			# print(i, pos[i], L[i])
	# 			pos[i] += L[i]
	# 			hits += 1
	# 		j += 1
	# 	# print(pos, hits)
	# 	i += 1
	# i, j = 0, 1
	# while i < n-1:
	# 	j = i+1
	# 	while j < n:
	# 		if pos[i] <= pos[j] and W[i] > W[j]:
	# 			# if W[i] < W[j]:
	# 			# 	continue	
	# 			# else:
	# 			# print(i, pos[i], L[i])
	# 			pos[i] += L[i]
	# 			hits += 1
	# 		j += 1
	# 	# print(pos, hits)
	# 	i += 1
	print(hits)     