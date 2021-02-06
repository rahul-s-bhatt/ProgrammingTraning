itemSold, noOfDays = map(int, input().split())

l = []

for i in range(itemSold):
	l.append(list(map(int, input().split())))

for i in l:
	for j in i:
		print(i, j)