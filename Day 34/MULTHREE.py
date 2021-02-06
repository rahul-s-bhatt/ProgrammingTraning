range = xrange
input = raw_input

for _ in range(int(input())):
	k, d0, d1 = map(int, input().split())

	currSum = (d0 + d1)
	nextDigit = currSum % 10
	currSum += nextDigit
	
	i = k - 3

	if k == 2:
		if currSum % 3 == 0:
			print "YES"
		else:
			print "NO"
		continue

	while i > 0:
		if nextDigit == 6:
			sets = i//4
			currSum += 20 * (sets)
			i -= (sets * 4)

			if i == 0:
				pass
			elif i == 1:
				currSum += 2
			elif i == 2:
				currSum += 6
			elif i == 3:
				currSum += 14
			i =0
			break

 		elif nextDigit == 0:
 			i = 0
			break
		else:
			nextDigit = (nextDigit * 2) % 10
			currSum += nextDigit
			i -= 1

	if currSum % 3 == 0:
		print "YES"
	else:
		print "NO"