N = 12

count = 0

for i in range(N):
	for j in range(N):
		sn = (i+j)*((j-i+1)//2)
		if sn == N:
			count += 1

print(count)