import sys, math

def solve(n, luckyList):
	if n in luckyList:
		return "YES"
	else:
		for i in range(len(luckyList)):
			if((n-luckyList[i]) in luckyList):
				return "YES"
	return "NO"


sys.setrecursionlimit(10**7)

def I(): return int(sys.stdin.readline().rstrip())
def MI():return map(int, sys.stdin.readline().rstrip().split())
def LI():return list(map(int, sys.stdin.readline().rstrip().split()))
def LI2():return list(map(int, sys.stdin.readline().rstrip()))
def S():return sys.stdin.readline().rstrip()
def LS():return list(sys.stdin.readline().rstrip().split())
def LS2():return list(sys.stdin.readline().rstrip())

for i in range(I()):
	n, lucky = MI()

	nos = LI()

	luckyList = [lucky]

	temp = lucky

	while temp < max(nos):
		temp += 10
		luckyList.append(temp)
	
	for i in nos:
		print(solve(i, luckyList))