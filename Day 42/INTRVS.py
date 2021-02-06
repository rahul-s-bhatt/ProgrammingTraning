def solve(n, k, arr):
	solved = 0
	for i in arr:
		if i == -1:
			solved += 1

	if solved>(n//2):
		return "Rejected"

	for i in arr:
		if i > k:
			return "Too Slow"
	
	solved = 0
	for i in arr:
		if i == 1 or i == 0:
			solved += 1

	if solved == n:
		return "Bot"

	return "Accepted"

for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))

	print(solve(n, k, arr))