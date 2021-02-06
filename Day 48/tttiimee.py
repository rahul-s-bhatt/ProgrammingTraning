from datetime import datetime

def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    else: #Over midnight
        return nowTime >= startTime or nowTime <= endTime


timeStart = '04:12AM'
timeEnd = '04:12AM'
timeNow = '04:12PM'
timeEnd = datetime.strptime(timeEnd, "%I:%M%p")
timeStart = datetime.strptime(timeStart, "%I:%M%p")
timeNow = datetime.strptime(timeNow, "%I:%M%p")

print(isNowInTimePeriod(timeStart, timeEnd, timeNow))