# Problem 1
"""
Link: https://www.hackerearth.com/practice/algorithms/dynamic-programming/bit-masking/tutorial/

There is a new food delivery startup in town.
For simplicity, assume that there are N delivery executives
and N orders. Also we have estimated how much it would cost
the startup if delivery executive ‘i’ delivers the order ‘j’.
This considers all factors such as distance, traffic,
customer priority, food value etc.
Given a NxN cost matrix, we need to assign each order
to an executive in such a way that the total cost to the
startup is minimum.
Note that each order is to be allotted to a single executive,
and each executive will be allotted only one order.
"""








# Solution:
"""
	Brute force

Assign each executive and take the minimum total cost

assigned = [0] * N

(n=5, cost, assigned=bitmask)

assigned = [1, 0, 1, 1, 0] implies that tasks 0, 2, 3 has been
assigned to the first 3 persons.

for i in range(N):
	for j in range(N):
		if j not in assined:
			assined.add(j)
			total = min(total, cost[i][j]+i)
			assined.remove(j)

"""

"""
	DP or Cache
"""

"""
"""