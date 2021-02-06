t = int(input())
for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    arr = sorted(arr)

    result = 99999999

    for i in range(len(arr)-1):
        compute = (arr[i] & arr[i+1]) ^ (arr[i] | arr[i+1])
        result = min(result, compute)
    print(result)