N = int(input())
l = [input() for i in range(N)]

ans = 1

for i in range(N):
	if l[i] == "OR":
		ans += 1 << (i+1)
print(ans)