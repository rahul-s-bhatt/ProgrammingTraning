import sys
from bisect import bisect_left, bisect_right

t, n, m = map(int, input().split())

contest = []

for _ in range(t):
	contest.append(tuple(map(int,input().split())))

V = list(map(int, input().split()))
W = list(map(int, input().split()))

minSum = sys.maxsize

V.sort()
W.sort()

for i in contest:
	j = bisect_right(V, i[0]) - 1
	k = bisect_left(W, i[1])
	if j != -1 and k != len(W):
		minSum = min(minSum, (W[k]-V[j])+1)

print(minSum)

