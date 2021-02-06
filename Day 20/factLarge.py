n = int(input())
end = 0
carry = 0

arr = [-1] * 100000
arr[0] = 1

for i in range(2, n+1):
	for j in range(end+1):
		mul = arr[j] * i + carry
		arr[j] = mul % 10
		carry = mul // 10

	while carry != 0:
		end += 1
		arr[end] = carry % 10
		carry = carry // 10

for i in range(end, -1, -1):
	print(arr[i], end="")