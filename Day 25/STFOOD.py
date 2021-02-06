import sys

# input = sys.stdin.readline
# print = sys.stdout.write 

t = int(input())

for _ in range(t):
	
	n = int(input())
	maxProfit = -1

	profit = []

	for _ in range(n):
		s, p, v = map(int, input().split())
		profit.append((p//(s+1))*v)

	print(max(profit))