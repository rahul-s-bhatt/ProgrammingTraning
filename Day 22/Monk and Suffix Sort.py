s, n = input().split()
n = int(n)
l = []
j = len(s) - 1

while( j >= 0):
    s1 = ""
    s1 += s[j:]
    l.append(s1)
    j -= 1

l = sorted(l)
print(l[n-1])