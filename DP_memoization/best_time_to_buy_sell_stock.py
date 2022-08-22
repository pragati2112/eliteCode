import math
def best_time_to_buy_sell(prices):

	dp = [0]*len(prices)
	for i in range(1, len(prices)):
		dp[i] = prices[i]-prices[i-1]

		if prices[i] > prices[i-1]:
			prices[i] = prices[i-1]

	return max(dp)



def max_sub_array_sum(nums):
	max_sum = -math.inf
	temp = 0

	for num in nums:
		temp = max(temp+num, num)
		if temp>max_sum:
			max_sum = temp
	return max_sum				


print(best_time_to_buy_sell([7,1,3,5,6,4]))	