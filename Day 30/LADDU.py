import sys

range = xrange
input = raw_input

d = {"CONTEST_WON": 300, "TOP_CONTRIBUTOR": 300, "CONTEST_HOSTED": 50, "INDIAN": 200, "NON_INDIAN": 400}


for _ in range(int(input())):
	n, indian = input().split()
	n = int(n)

	activites, res = [], 0
	for _ in range(n):
		activites.append(input().split())

	for i in activites:
		if i[0] in d:
			if i[0] == "CONTEST_WON":
				if int(i[1]) <= 20:
					res += (d[i[0]] + (20 - int(i[1])))
				else:
					res += d[i[0]] 
			else:
				res += d[i[0]]
		else:
			res += int(i[1]) 

	print res//d[indian]