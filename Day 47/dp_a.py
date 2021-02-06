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

N = I()

ht = LI()

dp = [-1] * N

dp[0] = 0
dp[1] = abs(ht[0]-ht[1])

for i in range(2, N):
	dp[i] = min(dp[i-1]+abs(ht[i]-ht[i-1]), dp[i-2]+abs(ht[i]-ht[i-2]))

print(dp[N-1])