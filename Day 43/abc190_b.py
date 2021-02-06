yes = "No"

n, s, d = map(int, input().split())

l = []

for _ in range(n):
	x, y = map(int, input().split())
	l.append([x,y])
for i in l:
	if i[0]<s and i[1]> d:
		yes = "Yes"
		break

if yes=="No":
	print("No")
else:
	print(yes)