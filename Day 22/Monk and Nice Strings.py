t = int(input())

l = []

for _ in range(t):
    s1 = input()
    l.append(s1)
    if len(l) > 1:
        c = 0
        for j in l:
            if s1 > j:
                c += 1
        print(c)
    else:
        print(0)