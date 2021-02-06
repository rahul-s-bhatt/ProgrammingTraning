import itertools

N, M = map(int, input().split())
cond = [tuple(map(int, input().split())) for i in range(M)]
K = int(input())
choice = [tuple(map(int, input().split())) for i in range(K)]
ans = 0

# itertools.product()
# cartesian product, equivalent to a nested for-loop

# print('\n\n\n\n\n')
# print(*choice)


# print('\n\n\n\n\n')
# for balls in itertools.product(*choice):
# 	print(balls)


# creating all combination of the subsets

for balls in itertools.product(*choice):
    balls = set(balls)
    cnt = sum(A in balls and B in balls for A, B in cond)
    if ans < cnt:
        ans = cnt

print(ans)

# 0.8449s

# https://docs.python.org/3/library/itertools.html


# itertools.product(choice)
# output:
# ((1,2),)
# ((1,3),)
# ((2,3),)

# *choice - * is unpack operator

# itertools.product(*choice)
# output:
# (1,1,2)
# (1,1,3)
# (1,3,2)
# (1,3,3)
# (2,1,2)
# (2,1,3)
# (2,3,2)
# (2,3,3)