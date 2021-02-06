N = int(input())
arr = list(map(int, input().split()))

arr.sort()

res = 0

for i in range(N-1):
	res += (arr[i+1]-arr[i])*(N-1-i)*(i+1)

print(res)

# from itertools import combinations

# N = int(input())
# arr = list(map(int, input().split()))

# c = combinations(arr,2)

# res = 0
# for i in c:
# 	res += abs(i[0]-i[1])

# print(res)

# TLE