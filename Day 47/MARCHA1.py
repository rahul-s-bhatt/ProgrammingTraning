def solve(notes, demand, n):
	for bit in range(1<<n):
		res = 0
		for j in range(n):
			if bit&(1<<j):
				res += notes[j]
		if res == demand:
			return "Yes"
	return "No"

import sys

from itertools import chain, combinations

def powerset(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def p(notes, demand, n):
	multiset = set(powerset(notes))
	for s in multiset:
		if sum(s) == demand:
			return "Yes"
	return "No"

sys.setrecursionlimit(10**7)

def I(): return int(sys.stdin.readline().rstrip())
def MI():return map(int, sys.stdin.readline().rstrip().split())
def LI():return list(map(int, sys.stdin.readline().rstrip().split()))
def LI2():return list(map(int, sys.stdin.readline().rstrip()))
def S():return sys.stdin.readline().rstrip()
def LS():return list(sys.stdin.readline().rstrip().split())
def LS2():return list(sys.stdin.readline().rstrip())

for _ in range(I()):
	n, demand = MI()

	notes = [I() for _ in range(n)]

	# print(solve(notes, demand, n)) # 13.8 seconds
	print(p(notes, demand, n)) # 6 seconds