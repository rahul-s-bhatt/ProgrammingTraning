def solve(alcohol, K):
	res = 0
	c = 0

	for v, p in alcohol:
		res += (v*p)

		if res>(K*100):
			c+=1
			return c
		c += 1

	return -1

N, K = map(int, input().split())

alcohol = [tuple(map(int, input().split())) for i in range(N)]

# print(alcohol)

print(solve(alcohol, K))