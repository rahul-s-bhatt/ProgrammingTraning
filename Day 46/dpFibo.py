from functools import lru_cache
import time

def fact(n):
	f = [0, 1]
	for i in range(2, n+1):
		f.append(f[i-1]+f[i-2])
	return f[n]
	
for _ in range(int(input())):
	start_time = time.time()
	print(fact(int(input())))
print("--- %s seconds --- " % (time.time()-start_time))

# fact(10)
# some no <-- take 11 recursive calls, since none cached

# fact(5)
# just looks up cached value result