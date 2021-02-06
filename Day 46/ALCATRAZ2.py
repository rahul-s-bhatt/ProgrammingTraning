import sys

import itertools

sys.setrecursionlimit(10**7)

def I(): return int(sys.stdin.readline().rstrip())
def MI():return map(int, sys.stdin.readline().rstrip().split())
def LI():return list(map(int, sys.stdin.readline().rstrip().split()))
def LI2():return list(map(int, sys.stdin.readline().rstrip()))
def S():return sys.stdin.readline().rstrip()
def LS():return list(sys.stdin.readline().rstrip().split())
def LS2():return list(sys.stdin.readline().rstrip())
def T():return tuple(map(int, sys.stdin.readline().rstrip().split()))

arr = LI()
pairs = [MI() for _ in range(I())]
n = len(pairs)

allcombo = set(list(itertools.combinations(arr, 2)))

res = 0
ansMax = sys.minsize

for combo in allcombo:
	combo = set(combo)

	ansMax = max(res, ansMax)