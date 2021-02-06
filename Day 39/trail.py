for _ in range(int(input())):
	n, k = map(int, input().split())
	d = {i:0 for i in range(1, k+1)}
	arr = list(map(int, input().split()))

	types, maxLength, j= 0, 0, 0

	k -=1
	
	for i in range(n):
		d[arr[i]] += 1

		if d[arr[i]] == 1:
			types += 1

		while types > k:
			d[arr[j]] -= 1
			if d[arr[j]] == 0: types -= 1
			j += 1

		maxLength = max(i-j+1, maxLength)

	print(maxLength)