import timeit

start = timeit.default_timer()


curr, best = 0, 0

n, m = map(int, input().split())

conditions = []

# Am Bm
for _ in range(m):
	conditions.append(list(map(int,input().split())))

k = int(input())

people = []

# Ck Dk
for _ in range(k):
	people.append(list(map(int, input().split())))

# bitmasking

# to create all possible bitmasks
for mask in range(0, (1<<k)):
	balls_bitmasks = [0] * (n+1)
	for person in range(0, k):
		if mask&(1<<person):
			balls_bitmasks[people[person][0]] += 1
		else:
			balls_bitmasks[people[person][1]] += 1
	curr = 0
	for condition in conditions:
		if balls_bitmasks[condition[0]] and balls_bitmasks[condition[1]]:
			curr += 1

	best = max(best, curr)

print(best)

stop = timeit.default_timer()

print('Time: ', stop - start) 

# 1.4s