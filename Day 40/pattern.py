start, end = 4, 4

start -= 1

for i in range(end+1):
	print(str(start)*i)
	start += 1

start -= 1

for i in range(end-1, 0, -1):
	start-=1
	print(str(start)*i)