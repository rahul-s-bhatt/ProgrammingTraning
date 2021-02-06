for _ in range(int(input())):
	
	n = int(input())
	
	n2 = 2 * n
	
	a, b = 0, 0

	s = input()

	arr = [int(i) for i in s]
	i = 0
	while i<n2:
		if i%2 == 0:
			a += arr[i]
		else:
			b += arr[i]

		t = (n2 - i)

		if ((a-b) > (t//2)) or ((b-a) > ((t-1)//2)):
			print(i+1)
			break
		i += 1

	if a == b:
		print(n2)