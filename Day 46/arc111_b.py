import sys

sys.setrecursionlimit(10**7)

def I(): return int(sys.stdin.readline().rstrip())
def MI():return map(int, sys.stdin.readline().rstrip().split())
def LI():return list(map(int, sys.stdin.readline().rstrip().split()))
def LI2():return list(map(int, sys.stdin.readline().rstrip()))
def S():return sys.stdin.readline().rstrip()
def LS():return list(sys.stdin.readline().rstrip().split())
def LS2():return list(sys.stdin.readline().rstrip())

l = []

res = []

for _ in range(I()):
	l.append(LI())

res.append(l[0][0])

for i in l:
	if i[0] not in res:
		res.append(i[0])
	elif i[1] not in res:
		res.append(i[1])

print(len(res))