t, a, c = map(int, input().split())

if t == a:
	if c == 1:
		print("Takashi")
	else:
		print("Akoi")
else:
	if t>a:
		print("Takashi")
	else:
		print("Akoi")