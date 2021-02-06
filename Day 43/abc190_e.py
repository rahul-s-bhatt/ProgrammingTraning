from collections import deque

INF = 1 << 30

N, M = map(int, input().split())
g = [list() for i in range(N)]

for i in range(M):
	A, B = map(int, input().split())
	A -= 1
	B -= 1
	g[A].append(B)
	g[B].append(A)

K = int(input())
C = list(map(int, input().split()))

for i in range(K):
	C[i] -= 1

def BFS(s):
	cost = [INF] * N
	cost[s] = 0
	q = deque([s])
	# print("Deque at start: ",q)
	while q:
		# print("Deque inside: ",q)
		x = q.popleft()
		# print("Source: ",s, "X: ",x)
		for y in g[x]:
			# print("y in g[x]: ", y)
			if cost[y] == INF:
				cost[y] = cost[x] + 1
				# print("cost[x]: ", cost[x], "cost[y]: ", cost[y])
				q.append(y)
	# print([cost[c] for c in C])
	return [cost[c] for c in C]

cost = [BFS(c) for c in C]

dp = [[INF] * K for i in range(1<<K)]

for i in range(K):
	dp[1<<i][i] = 1

for bit in range(1<<K):
	for i in range(K):
		if dp[bit][i] == INF:
			continue
		for j in range(K):
			dp[bit | 1<<j][j] = min(dp[bit][i] + cost[i][j], dp[bit | 1<<j][j])

ans = min(dp[-1])+1

if ans == INF:
	ans = -1
print(ans)