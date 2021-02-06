import sys

sys.setrecursionlimit(10**7)

def I(): return int(sys.stdin.readline().rstrip())
def MI():return map(int, sys.stdin.readline().rstrip().split())
def LI():return list(map(int, sys.stdin.readline().rstrip().split()))
def LI2():return list(map(int, sys.stdin.readline().rstrip()))
def S():return sys.stdin.readline().rstrip()
def LS():return list(sys.stdin.readline().rstrip().split())
def LS2():return list(sys.stdin.readline().rstrip())

for i in range(I()):
	n = I()
	arr = LS()

	# Using Hashmap / Dictionary

	# Using a dict to store all the prefix as values
	# and suffix as keys
	
	d = {}

	for i in arr:
		if i[1:] in d:
			d[i[1:]].append(i[0])
		else:
			d[i[1:]]=[i[0]]


	# Now we'll store all the keys/suffixes in an list
	# not as set, since set isn't scriptable.

	allUniqueSuffixWords = list(d.keys())
	
	# now we'll just have to combine prefixes of other suffixes
	# thus creating a set[unique] prefixes and getting its length

	# this will create all unique prefixes, thus we'll have to
	# only subtract it from first set of prefixes and second set of prefixes
	# multiply them (getting no of multiple combinations)

	# thus answer will be multiplied by 2, creating more
	# set of team names with just funny words
	cnt = 0
	for i in range(len(d)):
		for j in range(i+1, len(d)):
			temp = len(set(d[allUniqueSuffixWords[i]]+d[allUniqueSuffixWords[j]]))
			cnt += (temp-len(d[allUniqueSuffixWords[i]]))*(temp-len(d[allUniqueSuffixWords[j]]))
	print(2*cnt)


	# Brute Force Algo

	# cnt = 0
	# i, j = 0, 1
	# swap1, swap2 = '', ''
	# while i < n-1:
	# 	j = i+1
	# 	while j < n:
	# 		swap1 = arr[i]
	# 		swap2 = arr[j]
	# 		if (swap2[0]+swap1[1:]) in arr or (swap1[0]+swap2[1:]) in arr:
	# 			pass
	# 		else:
	# 			cnt += 2
	# 		j += 1
	# 	i += 1

	# print(cnt)