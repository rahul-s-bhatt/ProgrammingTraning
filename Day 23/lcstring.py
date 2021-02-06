def lcstring(s1, s2, n, m):

	t = [[0 for x in range(n+1)] for x in range(m+1)]
	
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				t[i][j] = 0
			elif s1[i-1] == s2[j-1]:
				t[i][j] = 1 + t[i-1][j-1]
			else:
				t[i][j] = max(t[i-1][j], t[i][j-1])


	# index = t[n][m]
	
	t = ""

	# lcs = [""] * (index + 1)
	# lcs[index] = ""
	
	i, j = n, m	

	while(i > 0 and j > 0):
		if s1[i-1] == s2[j-1]:
			t += s1[i-1]
		else:
			if s1[i-1] > s2[j-1]:
				i -= 1
			else:
				j -= 1
	return t
	

s1 = "abcdef"
s2 = "acbef"

s = lcstring(s1, s2, len(s1), len(s2))
s = sorted(s, reverse = True)

print(s)