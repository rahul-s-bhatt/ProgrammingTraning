xrange = range
input = raw_input

def solve(arr, i, j, count):
	n = len(arr)

	if n == 1:
		return 1

	if j < n:
		
		if arr[i] <= arr[j]:
			return solve(arr, i+1, j+1, count+1)
		else:
			return solve(arr, i+1, j+1, count)
	
	return count


for _ in range(int(input())):
	n = int(input())

	arr = list(map(int, input().split()))

	print solve(arr, 0, 1, n)




# first learn to distingush betw 
# non-decreasing and strictly increasing.

# arr1 = [1, 1, 1, 2, 3, 4, 5, 6]
# arr2 = [1, 2, 3, 4, 5, 6]

# n1 = len(arr1)
# n2 = len(arr2)

# nonDecreasing = True
# strictlyIncreasing = True

# i, j = 0, 1

# while j<n1:
# 	if arr1[i] <= arr1[j]:
# 		i += 1
# 		j += 1
# 	else:
# 		nonDecreasing = False
# 		break

# if nonDecreasing:
# 	print "Non decreasing"
# else:
# 	print "Nothing"
