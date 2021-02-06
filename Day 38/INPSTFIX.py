from collections import deque

predence = {
	'^' : 3,
	'*' : 2,
	'/' : 2,
	'+' : 1,
	'-' : 1
}

for _ in range(int(input())):
	n = int(input())

	infix = input().strip()
	
	stack = deque()
	postfix = ""

	for i in infix:
		if 'A' <= i <= 'Z':
			postfix += i
		elif i == '(':
			stack.append(i)
		elif i == ')':
			topElem = stack.pop()

			while topElem != '(':
				postfix += topElem
				topElem = stack.pop()
		else:
			while stack and stack[-1] != '('and predence[stack[-1]] >= predence[i]:
				postfix += stack.pop()

			stack.append(i)

	while stack:
		postfix += stack.pop()

	print(postfix)