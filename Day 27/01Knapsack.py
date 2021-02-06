#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase

def knapsackMemo(W, wt, val, n):

    dp = [[-1 for i in range(W+1)] for j in range(n+1)]

    # base cond
    if n == 0 or W == 0: 
        return 0
    if dp[n][W] != -1:
        return dp[n][W]
    elif wt[n-1] <= W:
        dp[n][W] = max(val[n-1]+knapsackMemo(W-wt[n-1], wt, val, n-1), knapsackMemo(W, wt, val, n-1))
        return dp[n][W]

    else:
        dp[n][W] = knapsackMemo(W, wt, val, n-1)
        return dp[n][W]


def Knapsack(W, wt, val, n):

    if W == 0 or n == 0:
        return 0
    elif wt[n-1] <= W:
        return max(val[n-1]+Knapsack(W-wt[n-1], wt, val, n-1), Knapsack(W, wt, val, n-1))
    else:
        return  Knapsack(W, wt, val, n-1)

def main():
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)

    print(knapsackMemo(W, wt, val, n))

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