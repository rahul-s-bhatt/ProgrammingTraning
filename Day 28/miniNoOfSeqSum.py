import sys

s1 = []

def Count(arr, n, sum1):
	dp = [[0 for i in range(sum1+1)] for i in range(n+1)]
	
	for i in range(1, sum1+1):
		dp[0][i] = sys.maxsize - 1

	for i in range(1, n+1):
		for j in range(1, sum1+1):
			if arr[i-1] > j:
				dp[i][j] = dp[i-1][j]
			else:
				dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-arr[i-1]])

	return dp[n][sum1]

arr = [7,8,19,7,8,7,10,20]
sum1 = 38*2
n = len(arr)

print(Count(arr, n, sum1), s1)