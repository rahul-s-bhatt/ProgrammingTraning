# Stock Buy, Sell to maximize profit

# Observations: 1) n has be greater than or equal to 2.
# 				2) finding optimal buy and sell pairs
# 				has to non decreasing elements.

def stockBuySell(price, n):
	if n == 1:
		return
	
	i = 0
	# Step 1 : Finding local minima until i reaches end.
	while i < n-1:
		while i < n-1 and price[i+1] <= price[i]:
			i += 1

		if i == n-1:
			break

		buy = i
		i += 1

		# Step 2 : Finding local maxima if i reaches end, 
		# mark end as ending index.
		
		while i < n and price[i] >= price[i-1]:
			i += 1

		sell = i - 1
		
		# Step 3 : Updating the solution(increment count of buy sell pairs)
		# Step 4 : Repeat until end is not reached.

		print("Buy on day: ", buy, "\t", "Sell on day: ", sell)

price = [100, 180, 260, 310, 40, 535, 695]
n = len(price)

stockBuySell(price, n)

# Time complexity - O(n)