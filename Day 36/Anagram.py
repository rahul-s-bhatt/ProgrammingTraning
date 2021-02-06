# def find_anagram(words):
# 	sortedWords = [''.join(sorted(word)) for word in words]

# 	d = {}

# 	# {'abt': [0, 1], 'degins': [2, 3], 'cot': [4, 5]}
# 	for i, e in enumerate(sortedWords):
# 		d.setdefault(e, []).append(i)
# 	print(d)

# 	for index in d.values():
# 		print([words[i] for i in index])


anagramList = []

n = int(input())
arr = []
for _ in range(n):
	arr.append(input())
# find_anagram(arr)

for i in range(n):
	for j in range(n):
		
		if arr[i] == arr[j] or [arr[j], arr[i]] in anagramList:
			continue
		
		d = {}
		flag = 0
		
		for k in arr[i]:
			if k in d:
				d[k] += 1
			else:
				d[k] = 1
		
		for k in arr[j]:
			if k not in d:
				flag = 1
				break
			else:
				d[k] -= 1
		
		for k in d:
			if d[k] != 0:
				flag = 1
				break
		
		if flag == 0:
			anagramList.append([arr[i], arr[j]])

print(anagramList)

# s1 = input()
# s2 = input()

# d = {}
# flag = 0
# for i in s1:
# 	if i in d:
# 		d[i] += 1
# 	else:
# 		d[i] = 1

# for i in s2:
# 	if i not in d:
# 		flag = 1
# 		break
# 	else:
# 		d[i] -= 1

# for i in d:
# 	if d[i] != 0:
# 		flag = 1
# 		break

# if flag == 1:
# 	print("NO")
# else:
# 	print("YES")