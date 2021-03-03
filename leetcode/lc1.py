prices1 = [7,1,5,3,6,4]

prices2 = [7,6,4,3,1]

lis = []
for i in range(len(prices1)):
    for j in range(len(prices1)):
        if j > i:
            x = int(prices1[i])
            y = int(prices1[j])
            profit = y - x
            lis.append(profit)

num = max(lis)
if num < 0:
    num = 0
print(num)


	min_till_now = prices[0]
		max_profit = 0
		for price in prices[1:]:
			if price < min_till_now:
				min_till_now = price
			else:
				diff = price - min_till_now
				if max_profit < diff:
					max_profit = diff
		return max_profit
