from itertools import permutations, combinations 

perm = list(permutations('ENVIRONMENT'))
# comb = list(combinations([1, 1, 1, 4, 5]))

print(len(perm))

for i in perm:
	print(''.join(i))