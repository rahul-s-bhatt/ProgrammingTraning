import sys

range = xrange
input = raw_input

for _ in range(int(input())):
	for g in range(int(input())):
		I, N, Q = map(int, input().split())

		# Q, I -> 1-H, 2-T
		
		if not N % 2 or I == Q:
			print N >> 1
			continue
		print (N >> 1)+1
