import string

alpha = string.ascii_lowercase

s = input()

for i in s:
	print(alpha[int(i)],end="")