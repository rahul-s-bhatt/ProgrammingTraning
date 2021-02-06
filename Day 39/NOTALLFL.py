for _ in range(int(input())):
	n, k = map(int, input().split())

	arr = list(map(int, input().split()))

	# Creating a hash map for storing frequency of types of cakes
	d = {i:0 for i in range(1, k+1)}

	maxLength, types, j = 0, 0, 0

	k -= 1

	for i in range(n):
		d[arr[i]] += 1

		if d[arr[i]] == 1:
			types += 1

		while types > k:
			d[arr[j]] -= 1
			if d[arr[j]] == 0:
				types -= 1
			j += 1
			
		maxLength = max(maxLength, i-j+1)

	print(maxLength)