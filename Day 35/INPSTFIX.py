from collections import deque
import string

range = range
input = input

precedence = {
	"^" : 4,
	"/" : 3,
	"*" : 3,
	"+" : 2,
	"-" : 2,
	"(" : 1
}

for _ in range(int(input())):
	stack = deque()

	n = int(input())

	s = input()

	res = ""

	for i in s:
		if i in string.uppercase:
			# res += i
			print(i, end="")
		else:
			if i == ")":
				while i != '(':
					print(i,end="")
					stack.pop()
			else:
				stack.append(i)