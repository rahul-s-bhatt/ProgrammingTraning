a, b, c = map(int, input().split())

if c == 0:
	# Takahashi
	if a>b:
		print("Takahashi")
	else:
		print("Aoki")
else:
	# Aoki
	if b>a:
		print("Aoki")
	else:
		print("Takahashi")