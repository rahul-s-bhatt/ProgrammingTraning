from functools import lru_cache
import time

@lru_cache(maxsize=128)
def fact(n):
	return n*fact(n-1) if n else 1

for _ in range(int(input())):
	start_time = time.time()
	print(fact(int(input())))
print("--- %s seconds --- " % (time.time()-start_time))

# fact(10)
# some no <-- take 11 recursive calls, since none cached

# fact(5)
# just looks up cached value result