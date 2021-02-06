from collections import deque

range = range
input = input

n, k = map(int, input().split())

arr = list(map(int, input().split()))

f = 1

arr = arr[::-1]

stack = deque()

for i in range(n):
	if not stack:
		stack.append([arr[i], i])
	else:
		while stack and stack[-1][0] >= arr[i]:
			stack.pop()

		if not stack:
			f *= 1
		else:
			f *= (i-stack[-1][1]+1)
			f = f%1000000007
	stack.append([arr[i], i])

	# print(i,"th iteration: ",stack, f)
del stack
print(f)