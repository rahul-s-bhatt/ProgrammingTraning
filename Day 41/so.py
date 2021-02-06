n, k = input().split()
k = int(k)

n = [int(i) for i in n]

n[:k], n[k:] = n[-k:], n[:-k]

print(''.join(map(str, n)))