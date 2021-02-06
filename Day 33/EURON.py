import sys

range = xrange
input = raw_input

n = int(input())

arr = list(map(int, input().split()))

start, end = 0, n - 1

count = 0

mid = start + (end - start) // 2

end = mid

while start <= end:
	mid = start + (end - start) // 2
	if arr[mid] < arr[start]:
		count += mid
		start += 1
	else:
		end -= 1

start = mid
end = n-1

while start <= end:
	mid = start + (end - start) // 2
	if arr[mid] > arr[end]:
		count += end
		end -= 1
	else:
		start += 1

start = mid + 1
end = n-1
while start <= end:
	if arr[start] < arr[end]:
		count -= 1
		end -= 1
	else:
		start += 1

print count