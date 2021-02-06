import sys

range = xrange
input = raw_input

for _ in range(0, int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    if sum(arr)<(2*k) or n < 2:
        print -1
    elif sum(arr) == (2*k):
        print n
    else:
        ulta = sorted(arr, reverse=True)

        max1 = ulta[0]
        max2 = ulta[1]

        if max1 >= k and max2 >= k:
            print(2)
            break
        
        arr=sorted(arr)
        count = n
        sum1 = sum(arr)

        for i in arr:
            if sum1-i < (2*k):
                sum1 -= i
                count -= 1
                break
            else:
                sum1 -= i
                count -= 1

        print(count+1)