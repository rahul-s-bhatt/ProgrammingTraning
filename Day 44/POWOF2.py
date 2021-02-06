import math

def solve(x, count):
	
	if x == 1:
		return count
	
	count += 1

	x = int(math.log(x, 2))

	if x&(x-1)!=0 and x!=1:
		return count
	
	return solve(x, count)

for _ in range(int(input())):
	x = int(input())
	count = 0
	if x&(x-1)!=0:
		print(0)
	else:
		print(solve(x, count))