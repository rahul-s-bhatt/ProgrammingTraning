import sys

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
	s = ''
	for i in range(1, n+2):
		for j in range(1, i):
			if j == i-1:
				s+=str(j)
			else:
				s+=str(j)+'*'
		s+='\n'
	print(s)