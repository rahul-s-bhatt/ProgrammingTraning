for _ in range(int(input())):

	l, r = map(int, input().split())

	diff = l-r

	dp = [0] * r

	dp[0] = 1
	dp[1] = 3

	for i in range(2, r):
		dp[i] = dp[i-1] + (i+1)

	print(dp[r-2])