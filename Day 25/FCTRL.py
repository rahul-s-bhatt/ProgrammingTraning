import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

for _ in range(n):
	a = int(input())
	s = 0
	while a > 0:
		s += a // 5
		a //= 5
	s = str(s) + "\n"
	print(s)