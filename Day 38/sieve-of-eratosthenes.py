def SieveOfEratosthenes(n):
	# step 1 : Create bool arr with True val till n+1
	prime = [True for _ in range(n+1)]

	# step 2 : iterate from 2, and make all the multiple
	# of 2, 3, 5, 7... False.
	i = 2

	while i*i <= n:
		
		if prime[i]:
			for j in range(i*i, n+1, i):
				prime[i] = False
		i += 1

	prime[0], prime[1] = False, False

	return prime