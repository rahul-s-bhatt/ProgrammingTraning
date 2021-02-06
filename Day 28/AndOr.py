for _ in range(int(input())):

	n, m = map(int, input().split())

	a = list(map(int, input().split()))
	b = list(map(int, input().split()))

	temp = 0

	v = {0}

	# i, j = 0, 0

	# while i<n and j<m:		
	# 	if i<n:
	# 		v.add(temp|a[i])
	# 		temp = temp|a[i]	
	# 		i += 1
	# 	if j<m:
	# 		v.add(temp&b[j])
	# 		temp = temp&b[j]
	# 		j += 1


	for i in a:
		v.add(temp|i)
		temp = temp|i

	for i in b:
		v.add(temp&i)
		temp = temp&i

	maxx = max(v)

	for i in a:
		if i <= maxx and i not in v:
			v.add(i)

	for i in b:
		if i <= maxx and i not in v:
			v.add(i)

	print(len(v))