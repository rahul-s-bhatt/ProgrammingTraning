#!/usr/bin/env python
import os
import sys
import numpy as np

# import time

from io import BytesIO, IOBase

def part(arr, n, k):
	count = 0
	dp = np.zeros((n+1, k+1))

	for i in range(n+1):
		dp[i][0] = 1

	for i in range(1, n+1):
		for currSum in range(1, k+1):
			# exclude current elem
			dp[i][currSum] = dp[i-1][currSum]

			# include current elem
			if(arr[i-1] <= currSum):
				dp[i][currSum] = (dp[i][currSum] or dp[i-1][currSum-arr[i-1]])

	i = n
	currSum = k

	sum1, sum2 = 0, 0

	while(i > 0 and currSum >= 0):

		# if curr elem does not contribute to k, then
		# add it set 2
		if(dp[i-1][currSum]):
			i -= 1
			if sum1 < k:
				sum1 += arr[i]
				count += 1
			else:
				pass

		# if curr elem contribute
		# to k then it belongs to set 1
		elif (dp[i-1][currSum - arr[i-1]]):
			i -= 1
			currSum -= arr[i]
			if sum2 < k:
				sum2 += arr[i]
				count += 1
			else:
				pass
	return count

def main():
    # start_time = time.time()
    for _ in range(0, int(input())):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        arr=sorted(arr)
        if sum(arr)%2!=0 and sum(arr)<=(2*k):
            print(-1)
        elif sum(arr) == (2*k):
        	print(n)
        else:
            if arr[n-1]>k and arr[n-2]>k and n>=1:
                print(arr[0])
            else:
                print(part(arr, n, k))
    # print("--- %s seconds ---" % (time.time() - start_time))

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