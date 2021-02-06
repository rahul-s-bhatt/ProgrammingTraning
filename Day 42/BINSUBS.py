from collections import deque

for _ in range(int(input())):
	n = int(input())

	arr = input()

	stack = deque()

	stack.append(arr[0])
	
	c = 0

	for i in range(1, n):
		if stack and stack[-1] == '1' and arr[i] == '0':
			stack.pop()
			c += 1
		else:
			stack.append(arr[i])

	print(c)