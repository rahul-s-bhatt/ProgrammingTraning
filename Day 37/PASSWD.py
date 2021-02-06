import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['@', '#', '%', '&', '?']

# Only lower can be first n last

for _ in range(int(input())):

	st = input()

	l, u, d, s = 0, 0, 0, 0
	n = len(st)

	for i in range(n):
		if st[i] in upper and i>0 and i<n-1:
			u = 1
		if st[i] in digit and i>0 and i<n-1:
			d = 1
		if st[i] in special and i>0 and i<n-1:
			s = 1
		if st[i] in lower:
			l = 1
	if u and d and l and s and len(st) >= 10:
		print("YES")
	else:
		print("NO")