#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase

def part(arr, k, n, length):
	# sum1 = (2*k)

	# if n == 0:
		# return length
	sum1 = 0
	c = 0
	miniLen = sys.maxsize

	for i in range(n):
		# length = 1
		sum1 = 0
		c = 0
		for j in range(n):
			if j == i:
				continue
			if sum1 >= k:
				break
			else:
				sum1 += arr[i]+arr[j]
				c += 1
				# miniLen = min(miniLen, c)
		print(c)
	return c
			# if sum(arr[j:length]) >= sum1:
				# return length
			# else:
				# length += 1
	# length = part(arr, k, n, length+1)

	# return length

def main():
	arr = [7,8,19,7,8,7,10,20]
	# arr = [2, 10, 9, 4]
	k = 38
	# k = 5
	n = len(arr)
	# s= part(arr, k, n, 1)

	sum1 = 0
	arr = sorted(arr, reverse=True)
	c = 0

	temp = []
	j = 0
	for i in arr:
		if sum1 >= (2*k):
			break
		sum1 += i
		temp.append(i)
		j += 1
		c += 1

	while sum1 > (2*k) and j<n:
		sum1 -= arr[j]
		c -= 1
		j += 1

	# if sum1 < (2*k):
	# 	# add minimum element
	# 	print(arr[c-1], sum1)
	# 	sum1 += arr[c-1]
	# 	temp.append(arr[c-1]) 
	# 	c -= 1

	print(temp, (2*k), sum1, c+1)

	# print(part(arr, k, n, 1))

# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()