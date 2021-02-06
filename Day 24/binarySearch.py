arr = [1, 12, 12, 12, 13, 13, 13, 16, 25, 46]
x = 12

def binarySearch(arr, x):
	low = 0
	end = len(arr) - 1
	while low <= end:
		mid = (low + end) // 2
		if x == arr[mid]:
			print(arr[mid], mid+1)
			break
		elif x > arr[mid]:
			low = mid + 1
		else:
			end = mid - 1

def firstnLastElemSortedArray(arr, x):
	firstPos = len(arr)
	low = 0
	end = len(arr) - 1

	while low <= end:
		mid = low + (end - low) // 2
		if x >= arr[mid]:
			firstPos = mid
			end = mid - 1
		else:
			low = mid + 1

	return firstPos

# binarySearch(arr, x)

f = firstnLastElemSortedArray(arr, x)
l = firstnLastElemSortedArray(arr, x+1) - 1

if (f <= l):
	return [f, l]
return [-1, -1]