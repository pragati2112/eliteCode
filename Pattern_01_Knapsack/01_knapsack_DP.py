def knapsack(weights, profits, capacity):
	n = len(profits)
	dp = [[0 for i in len(capacity)+1] 0 for y in range(n)]

	# filled 1st column
	for i in range(0,n):
		dp[i][0] = 0

	
	# fill 1st row--
	for c in range(0, capacity+1):
		if weights[0]<=c:
			dp[0][c] = profits[0]


	# start with 2nd row--
	for i in range(1,n+1):
		for c in range(1, capacity+1):
			profit1, profit2 = 0,0 
			if weights[i] <=c:
				profit1 = profits[i]+dp[i-1][c-weights[i]]

			profit2 = dp[i-1][c]

			dp[i][c] = max(profit1, profit2)


	return dp[n-1][capacity]



def equal_subset_sum_partition(nums):
	s = sum(num)

	s = int(s/2)
	n=len(nums)

	dp = [[False for x in range(s+1)] False for y in range(nums)]

	for i in range(0, n):
		dp[i][0] = True

	for j in range(0, s+1):
		dp[0][j]=num[0]==j

	
	for i in range(0,n):
		for j in range(0, s+1):
			if dp[i-1][j]:
				dp[i][j] = dp[i-1][j]

			elif j>=nums[i]:
				dp[i][j] = dp[i-1][j-nums[i]]

	return dp[n-1][s]



def equal_subset_sum(nums , s):
	n=len(nums)

	dp = [[False for x in range(s+1)] False for y in range(nums)]

	for i in range(0, n):
		dp[i][0] = True

	for j in range(0, s+1):
		dp[0][j]=num[0]==j

	
	for i in range(0,n):
		for j in range(0, s+1):
			if dp[i-1][j]:
				dp[i][j] = dp[i-1][j]

			elif j>=nums[i]:
				dp[i][j] = dp[i-1][j-nums[i]]

	return dp[n-1][s]				




def min_sum_diffrence(nums):
	s = sum(num)
	n = len(nums)
	dp = [[False for x in range((s/2)+1)] False for y in range(n) ]

	for i in range(n):
		dp[i][0] = True

	
	for j in range((s/2)+1):
		dp[0][j] = nums[0]==s/2

	
	for i in range(1, n):
		for j in range(1, (s/2)+1):
			if dp[i-1][j]:
				dp[i][j] = dp[i-1][j]

			elif j>=nums[i]:
				dp[i][j] = dp[i-1][j-nums[i]]

	sum1, sum2 = 0, 0

	for i in range(s/2,-1,-1):
		if dp[n-1][i]:
			sum1 = i
			break
	sum2 = s-sum1	
	return abs(sum2-sum1)	

