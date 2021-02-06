from bisect import bisect_left, bisect_right

def BinarySearchUpperBound(a, x): 
    i = bisect_left(a, x) 
    if i: 
        return (i-1) 
    else: 
        return -1

def BinarySearchLowerBound(a, x): 
    i = bisect_right(a, x) 
    if i: 
        return (i-1) 
    else: 
        return -1


def just_smaller(a, e):
    pos = -1
    low = 0
    high = len(a)-1
    while low <= high:
        mid = (high+low)//2
        if a[mid] <= e:
            pos = a[mid]
            low = mid + 1
        else:
            high = mid - 1
    return pos

def just_greater(a, e):
    pos = -1
    low = 0
    high = len(a)-1
    while low <= high:
        mid = (high+low)//2
        if a[mid] >= e:
            pos = a[mid]
            high = mid - 1
        else:
            low = mid + 1
    return pos

a  = [2,4,14,26] 
b = [13, 21]

x = 15
y = 21

res = BinarySearchLowerBound(a, x) 
if res == -1: 
    print("No value smaller than ", x) 
else: 
    print("Largest value smaller than ", x, " is ", a[res])

res = BinarySearchLowerBound(b, y) 
if res == -1: 
    print("No value smaller than ", y) 
else: 
    print("Largest value smaller than ", y, " is ", b[res])

res = just_smaller(a, x)
print(res)
res = just_greater(b, y)
print(res)