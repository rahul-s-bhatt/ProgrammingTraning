import sys, math

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

	sortedW = sorted(W)

	for i in range(1, n):
		currentPosInUnsorted = W.index(sortedW[i])
		prevPosInSorted = pos[W.index(sortedW[i-1])]

		temp = currentPosInUnsorted

		while temp<=prevPosInSorted:
			temp += L[currentPosInUnsorted]
			pos[currentPosInUnsorted] = temp
			hits += 1
	
	print(hits)     