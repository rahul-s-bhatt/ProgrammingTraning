import sys
from itertools import chain, combinations

def powerset(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

sys.setrecursionlimit(10**7)

def I(): return int(sys.stdin.readline().rstrip())
def MI():return map(int, sys.stdin.readline().rstrip().split())
def LI():return list(map(int, sys.stdin.readline().rstrip().split()))
def LI2():return list(map(int, sys.stdin.readline().rstrip()))
def S():return sys.stdin.readline().rstrip()
def LS():return list(sys.stdin.readline().rstrip().split())
def LS2():return list(sys.stdin.readline().rstrip())

N, K = MI()

ht = LI()

INF = float('inf')

dp = [INF] * N

dp[0] = 0

for i in range(N):
	for j in range(1, K+1):
		if i-j >= 0:
			dp[i] = min(dp[i], dp[i-j]+abs(ht[i]-ht[i-j]))
print(dp[N-1])