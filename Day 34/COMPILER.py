range = range
input = input

for _ in range(int(input())):
	s = input()
	length = 0
	maxLength = 0
	for i in range(len(s)):			
		if s[i] == '<':
			length += 1
		else:
			length -= 1
			if length<0:
				break
		
		if length == 0:
			maxLength = i+1

	print(maxLength)