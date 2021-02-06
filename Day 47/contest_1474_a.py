import sys
import itertools

def solve(n, s):
	maxD = ''
	
	tu = {}

	for i in itertools.product(range(2), repeat=n):
		j = 0
		res = ''
		while j<n:
			res += str(i[j]+int(s[j]))
			j += 1
		gby = [k for k,g in itertools.groupby(res)]
		d = ''.join(map(str, gby))
		maxD = max(d, maxD)
		if maxD not in tu: 
			tu[maxD] = i

	return tu[maxD]

	# res = ''
	# j = 0 

	# while j<n:
	# 	res += str(int(maxD[j])-int(s[j]))
	# 	j += 1
	
	# return res

sys.setrecursionlimit(10**7)

def I(): return int(sys.stdin.readline().rstrip())
def MI():return map(int, sys.stdin.readline().rstrip().split())
def LI():return list(map(int, sys.stdin.readline().rstrip().split()))
def LI2():return list(map(int, sys.stdin.readline().rstrip()))
def S():return sys.stdin.readline().rstrip()
def LS():return list(sys.stdin.readline().rstrip().split())
def LS2():return list(sys.stdin.readline().rstrip())

for _ in range(I()):
	n = I()
	s = S()

	print(''.join(map(str, solve(n, s))))