from bisect import bisect_left, bisect_right

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

print(find_lt([1,2,3,4], 4))
