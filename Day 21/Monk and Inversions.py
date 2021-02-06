t = int(input())

for i in range(t):
    n = int(input())

    arr = []
    for j in range(n):
        arr.append(list(map(int, input().split())))

    c = 0
    for x in range(n):
        for y in range(n):
            for p in range(n):
                for q in range(n):
                    if x <= p and y <= q:
                        if arr[x][y] > arr[p][q]:
                            c += 1
    print(c)