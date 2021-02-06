def b_expo(a, b):
	res = 1
	while b > 0:
		if b & 1:
			res *= a
		a *= a
		b >>= 1
	return res

def b_expo_mod(a, b, c):
	res = 1
	while b > 0:
		if b & 1:
			res = ((res % c) * (a % c)) % c
		a *= a
		b >>= 1
	return res

"""
* Wondering how this method works !
* It's pretty simple.
* Let's say you need to calculate a ^ b
* RULE 1 : a ^ b = (a*a) ^ (b/2) ---- example : 4 ^ 4 = (4*4) ^ (4/2) = 16 ^ 2
* RULE 2 : IF b is ODD, then ---- a ^ b = a * (a ^ (b - 1)) :: where (b - 1) is even.
* Once b is even, repeat the process to get a ^ b
* Repeat the process till b = 1 OR b = 0, because a^1 = a AND a^0 = 1
*
* As far as the modulo is concerned,
* the fact : (a*b) % c = ((a%c) * (b%c)) % c
* Now apply RULE 1 OR 2 whichever is required.
"""