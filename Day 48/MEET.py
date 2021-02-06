import sys, math
from datetime import datetime

def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    elif endTime > startTime: #Over midnight
        return nowTime >= startTime or nowTime <= endTime
    else:
    	return False if nowTime != startTime else True

sys.setrecursionlimit(10**7)

def I(): return int(sys.stdin.readline().rstrip())
def MI():return map(int, sys.stdin.readline().rstrip().split())
def LI():return list(map(int, sys.stdin.readline().rstrip().split()))
def LI2():return list(map(int, sys.stdin.readline().rstrip()))
def S():return sys.stdin.readline().rstrip()
def LS():return list(sys.stdin.readline().rstrip().split())
def LS2():return list(sys.stdin.readline().rstrip())

for i in range(I()):
	scheduleTime = S()
	time = [S() for _ in range(I())]

	scheduleTime = scheduleTime.replace(" ", "")

	res = ""

	for i in time:
		startTime, endTime = i[:8], i[9:]
		startTime = startTime.replace(" ", "")
		endTime = endTime.replace(" ", "")
		endTime = datetime.strptime(endTime, "%I:%M%p")
		startTime = datetime.strptime(startTime, "%I:%M%p")
		timeNow = datetime.strptime(scheduleTime, "%I:%M%p")
		if isNowInTimePeriod(startTime, endTime, timeNow):
			res += '1'
		else:
			res += '0'

	print(res)