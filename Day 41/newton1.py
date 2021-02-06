n, m = map(str, input().split())

if n=='R' or m=='R':
	print('R')
elif n=='J':
	print(m)
elif m=='J':
	print(n)
else:
	print('D')