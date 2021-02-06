import sys
# not myself, sort, multiply * index+1, print max
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
a = []

for _ in range(n):
	a.append(int(input()))

a.sort(reverse=True)

a = [(i+1) * a[i] for i in range(len(a))]

print(str(max(a)))