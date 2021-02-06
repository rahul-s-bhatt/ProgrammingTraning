from collections import deque

for _ in range(int(input())):
	n = int(input())

	arr = list(map(int, input().split()))

	stack = deque()

	dp = [0] * n

	# if n == 1, then dp[n-1] = 1
	dp[0] = 1
	stack.append(arr[0])
	
	# no concept of top elem in deque,
	# so do it manually.
	j = 0
	

	for i in range(1, n):
		topElement = stack[j]
		if stack and topElement <= arr[i]:
			stack.append(arr[i])
			j += 1
			dp[i] = dp[i-1] + len(stack)
		else:
			# pop all elements in stack
			while stack:
				stack.pop()
				j -= 1
			stack.append(arr[i])
			j += 1
			dp[i] = dp[i-1] + len(stack)

	print(dp[n-1])