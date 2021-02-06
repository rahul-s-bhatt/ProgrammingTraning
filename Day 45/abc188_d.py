from collections import defaultdict

N, C = map(int, input().split())

D = defaultdict(int)

for i in range(N):
	a, b, c = map(int, input().split())

	D[a] += c
	D[b+1] -= c

days = list(D.keys())
days.sort()

ans, cost = 0, 0

for i in range(len(days)-1):
	d1 = days[i]
	d2 = days[i+1]

	cost += D[d1]
	ans += min(C, cost)*(d2-d1)

print(ans)