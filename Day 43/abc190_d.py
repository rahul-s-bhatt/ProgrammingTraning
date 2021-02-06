N = int(input())

count = 0

i = 1

while (i*i)<=(2*N):
	if ((2*N)%i) == 0:
		a = (((2*N)//i)-i+1)
		if a%2==0:
			count += 1
		if (i*i)!=(2*N) and a%2==0:
			count += 1
	i += 1
print(count)