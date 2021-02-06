import sys, math

import itertools

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
	arr = LI()

	arr.sort()

	x, y, z = max(arr), arr[0], arr[1]

	res = abs(x-y)+abs(y-z)+abs(z-x)

	print(res)