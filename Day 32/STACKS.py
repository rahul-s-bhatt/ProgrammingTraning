import sys

range = xrange
input = raw_input

for _ in range(int(input())):

	n = int(input())

	arr = list(map(int, input().split()))

	newL = []

	newL.append(arr[0])

	j = 0
	currIndex = 0

	for i in range(1, n):

		# adding operation
		if arr[i] >= newL[j]:
			j += 1
			newL.append(arr[i])
		else:
		# 	# if you look closely, it has sorted
		# 	# numbers in newL which means
		# 	# binary search baby!

			start, end = 0, len(newL) - 1
			ans = -1
			# searching operation handled
			while start <= end:
				mid = start + (end - start) // 2
				if newL[mid] > arr[i]:
					ans = mid
					end = mid - 1
				else:
					start = mid + 1
			
			newL[ans] = arr[i]

	s = ' '.join(map(str, newL))
	print len(newL), s