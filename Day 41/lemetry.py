s = input()

d = {}

for i in s:
	if i not in d:
		d[i] = 1
	else:
		d[i] += 1

c=0

for i in d:
	if d[i] == 1:
		c += 1
print(c)

# alphaadida