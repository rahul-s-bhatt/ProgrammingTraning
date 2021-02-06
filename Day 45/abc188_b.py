N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = 0

for i in range(N):
	res += (A[i]*B[i])

if not res:
	print("Yes")
else:
	print("No")