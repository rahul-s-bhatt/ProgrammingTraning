from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))
    c = Counter(arr)

    maxht = c.most_common()

    diff = maxht[0][1] - maxht[len(maxht)-1][1]

    if diff == 0:
        print(-1)
    else:
        print(diff)