import sys

range = xrange
input = raw_input

s = input()
maxLength = -1

n = len(s)

for i in range(n):
	j = n-1

	while s[j] == s[i]:
		j -= 1

	if i == j and j>0:
		j -= 1

	maxLength = max(maxLength, abs(i-j))

print maxLength