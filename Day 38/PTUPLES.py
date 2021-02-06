range = xrange
input = raw_input

# step 1 : Create bool arr with True val till N+1
N = 1000001
prime = [True for _ in range(n+1)]

# step 2 : iterate from 2, and make all the multiple
# of 2, 3, 5, 7... False.
i = 2

while i*i <= N:
	
	if prime[i]:
		for j in range(i*i, N+1, i):
			prime[j] = False
	i += 1

# step 3 : 0, 1 are non prime number
prime[0], prime[1] = False, False

# step 4 : 0(1) soln, we need to store the ans
# since pow(10,6) for every test case. 
ans = [0] * N
count = 0

for i in range(5, N):
	if prime[i] and prime[i-2]:
		count += 1
	ans[i] = count

for _ in range(int(input())):
	n = int(input())
	print ans[n]