import sys

sys.setrecursionlimit(10**7)

def I(): return int(sys.stdin.readline().rstrip())
def MI():return map(int, sys.stdin.readline().rstrip().split())
def LI():return list(map(int, sys.stdin.readline().rstrip().split()))
def LI2():return list(map(int, sys.stdin.readline().rstrip()))
def S():return sys.stdin.readline().rstrip()
def LS():return list(sys.stdin.readline().rstrip().split())
def LS2():return list(sys.stdin.readline().rstrip())
def T():return tuple(map(int, sys.stdin.readline().rstrip().split()))


# below logic isn't mine, just testing the speed in py3
# thank you

# it passes with 3.69 seconds

def sieve(n):
	prime = [True for i in range(n+1)]
	p = 2
	while (p*p <= n):
		if (prime[p] == True):
			for i in range(p*2, n+1, p):
				prime[i] = False
		p += 1

	prime[0] = False
	prime[1] = False

	return prime

maxN = int(10e6)+5

prime = sieve(maxN)

ans = [0] * (maxN+1)

for i in range(1, maxN+1):
	ans[i] = ans[i-1]+(prime[i] and prime[i-2])

for _ in range(I()):
	n = I()
	print(ans[n])