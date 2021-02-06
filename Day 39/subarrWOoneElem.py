for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	j = 0

	l = []

	for i in range(n):
		if arr[i] < k:
			pass
		else:
			l.append(range(j, i))
			j = i

	# for i in l:
	# 	print(i)

	print(l)

	# if l:
	# 	maxL = 0
	# 	for i in l:
	# 		L = 0
	# 		for j in i:
	# 			L += 1
	# 		maxL = max(L, maxL)

	# 	print(maxL)
	# else:
	# 	print(n)