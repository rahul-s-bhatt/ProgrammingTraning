import sys

from itertools import permutations 

range = xrange
input = raw_input

for _ in range(int(input())):

	n = input()

	s = n

	for i in range(1, len(n)+1):
		temp = n[:i-1] + n[i:]

		s = min(int(s), int(temp))

	print s