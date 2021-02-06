from collections import deque

range = xrange
input = raw_input

n = int(input())
arr = list(map(int, input().split()))

depthCurr, depthNesting, depthLoc = 0, 0, 0 # depth vars
countBracks, cntLoc, maxCnt = 0, 0, 0 # count vars

outerBracketStartIndx = 0

for i in range(n):

	if not depthCurr:
		countBracks = 0
		outerBracketStartIndx = i+1

	if arr[i] == 1:
		depthCurr += 1
	else:
		depthCurr -= 1

	countBracks += 1

	if depthCurr > depthNesting:
		depthNesting = depthCurr
		depthLoc = i+1
	
	if countBracks > maxCnt:
		cntLoc = outerBracketStartIndx
		maxCnt = countBracks

print depthNesting, depthLoc, maxCnt, cntLoc