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

	unique = set()
	for i in arr:
		unique.add(i[0])

	arrSliced = set(i[1:] for i in arr)

	cnt = 0
	for i in arrSliced:
		for j in unique:
			if (j+i) in arr:
				continue
			else:
				cnt += 1

	print(cnt)

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