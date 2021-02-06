#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase


def lis(arr, x, y):

	sum1 = 0
	n = len(arr)

	lis = [1] * n

	for i in range(1, n):
		for j in range(0, i):
			if arr[i] > arr[j] and lis[i] < lis[j] + 1 and sum1 <= y:
				lis[i] = lis[j]+1
	maximum = 0
	print(lis)
	for i in range(n):
		maximum = max(maximum, lis[i])

	return maximum

def solve(arr, n, x, y):
    sum1 = 0
    i = 0
    # iterate without any swaps
    while i<n and sum1 <= y:
        if sum1 >= x and sum1 <= y:
            return 0
        else:
            sum1 += arr[i]
        i += 1

    if sum1 <= y and sum1 >= x:
        return 0
    else:
        # we need 1 swap, this swap we will do
        # smallest w max such that max < y
        maxSortedArr = sorted(arr, reverse=True)
        i = 1
        sum2 = 0
        j = 0
        maxElem = 0
        
        while j<n:
            if maxSortedArr[j] > y:
                pass
            else:
                maxElem = max(maxElem, maxSortedArr[j])
            j += 1

        indx = arr.index(maxElem)
        
        arr[0], arr[indx] = maxElem, arr[0]
        sum2 += arr[0]

        while i<n and sum2<=y:
            if sum2 >= x and sum2 <= y:
                return 1
            else:
                sum2 += arr[i]
            i += 1

    if sum2 <= y and sum2 >= x:
        return 1
    else:
        # we need 1 swap, this swap we will do
        # smallest w max such that max < y
        maxSortedArr = sorted(arr, reverse=True)
        i = 2
        j = 0
        sum3 = 0
        maxElem1, maxElem2 = 0, 0
        
        while j<n:
            if maxSortedArr[j] > y:
                pass
            else:
                maxElem1 = max(maxElem1, maxSortedArr[j])
                t = min(maxElem1, maxSortedArr[j])
                if t != maxElem1:
                    maxElem2 = max(maxElem2, min(maxElem1, maxSortedArr[j]))
            j += 1
        
        print(maxElem1, maxElem2)

        indx1 = arr.index(maxElem1)
        indx2 = arr.index(maxElem2)

        arr[0], arr[indx1] = arr[indx1], arr[0]
        sum3 += arr[0]
        
        arr[1], arr[indx2] = arr[indx2], arr[1]
        sum3 += arr[1]

        while i<n and sum3<=y:
            if sum3 >= x and sum3 <= y:
                return 2
            else:
                sum3 += arr[i]
            i += 1
    return -1

def main():

    for _ in range(int(input())):
        n, x, y = map(int, input().split())

        arr = list(map(int, input().split()))
        n = len(arr)

        # print(solve(arr, n, x, y))
        print(lis(arr, x, y))
        

    

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