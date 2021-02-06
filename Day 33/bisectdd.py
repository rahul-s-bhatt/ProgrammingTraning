from bisect import bisect_left, bisect_right

a = [1, 6, 7, 3, 2, 19, 17, 3]

x = 6

a = sorted(a)

print(a)

left = bisect_left(a, x)
right = bisect_right(a, x)

a.insert(left, x)

print(a)

a.remove(x)

a.insert(right, x)

print(a)