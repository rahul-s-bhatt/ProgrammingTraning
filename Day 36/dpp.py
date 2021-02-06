# Given 3 numbers {1, 3, 5}, we need to tell
# the total number of ways we can form a number 'N' 
# using the sum of the given three numbers.


def solve(n):
	d = {}
	if n < 1:
		return 0
	if n ==0 or n == 1:
		return 1
	if n not in d:
		d[n] = solve(n-1)+solve(n-3)+solve(n-5)

	return d[n]

print solve(7)