prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
n = int(input())
arr = list(map(int, input().split()))


for i in arr:
	if i in prime:
		print(i,end=" ")

for i in arr:
	if i not in prime:
		print(i, end=" ")