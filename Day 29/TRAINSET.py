import sys

from itertools import permutations 

range = xrange
input = raw_input

for _ in range(int(input())):

	totalWordsCount = int(input())
	
	l = []
	for i in range(totalWordsCount):
		l.append(input())

	setOfWords = set()

	for i in range(len(l)):
		setOfWords.add(str(l[i][:-2]))

	d = dict()

	for i in setOfWords:
		
		if i not in d:
			d[i] = 1
		else:
			d[i] += 1
		
		individualWordCount, countOfOnes = 0, 0
		for j in range(len(l)):
			print i, j
			if i == str(l[j][:-2]):
				individualWordCount += 1
				if int(l[j][-1]) == 1:
					countOfOnes += 1

		maxCount = max(totalWordsCount-countOfOnes, countOfOnes)
		d[i] = maxCount

	print d