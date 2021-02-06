def solve(n, arr):
	
	even, odd = 0, 0
	
	for i in arr:

		if i%2 == 0:
			even += 1
		else:
			odd += 1

	# if odd == 0 or even == 0:
	# 	return 0

	if odd > even:
		return even

	return odd

for _ in range(int(input())):
	n = int(input())
	arr = list(map(int, input().split()))
	
	print(solve(n, arr))