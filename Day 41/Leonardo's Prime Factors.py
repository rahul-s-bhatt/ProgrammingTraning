arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 57, 59]

for _ in range(int(input())):
	n = int(input())
	res = 1

	i = 0

	while res <= n:
		res *= arr[i]
		if res > n:
			print(i)
			break
		i += 1