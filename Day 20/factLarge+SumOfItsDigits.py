n = int(input())

arr = [-1] * 1000000
arr[0] = 1

end, carry = 0, 0

for i in range(2, n+1):
	for j in range(end+1):
		mul = arr[j] * i + carry
		arr[j] = mul % 10
		carry = mul // 10

	while carry != 0:
		end += 1
		arr[end] = carry % 10
		carry //= 10

s = 0
for i in range(end, -1, -1):
	s += arr[i]
	print(arr[i])
print("\n\n\n",s)