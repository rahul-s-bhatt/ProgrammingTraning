# Recursive code

range = xrange
input = raw_input

# def solve(n, lookup = {}):
	
# 	if n < 0:
# 		return 0
	
# 	if n == 2 or n == 3:
# 		return 1

# 	if n not in lookup:
# 		lookup[n] = (solve(n-2) + solve(n-3))

# 	return lookup[n]

for _ in range(int(input())):
	n = int(input())

	if n > 3:
		dp = [0] * (n+1)
		dp[0] = 1
		# dp[1] = 0
		dp[2] = 1

		for i in range(3, n+1):
			dp[i] = dp[i-2] + dp[i-3]
		print dp[n]
	else:
		if n == 2 or n == 3:
			print 1