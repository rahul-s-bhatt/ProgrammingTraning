n = int(input())

table = [0] * (n+1)

table[0] = 1

print("3\n")
for i in range(3, n+1):
	table[i] += table[i-3]
	print(table[i], table[i-3])

print("\n\n5\n")
for i in range(5, n+1):
	table[i] += table[i-5]
	print(table[i], table[i-5])

print("\n\n10\n")
for i in range(10, n+1):
	table[i] += table[i-10]
	print(table[i], table[i-10])

print(table[n])

"""
Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find number of ways to reach the given score.
Examples:

Input: n = 20
Output: 4
There are following 4 ways to reach 20
(10, 10)
(5, 5, 10)
(5, 5, 5, 5)
(3, 3, 3, 3, 3, 5)

Input: n = 13
Output: 2
There are following 2 ways to reach 13
(3, 5, 5)
(3, 10)


Solution:

This problem is a variation of coin change problem
and can be solved in O(n) time and O(n) auxiliary space.

The idea is to create a table of size n+1 to store counts
of all scores from 0 to n. For every possible move
(3, 5 and 10), increment values in table.

"""