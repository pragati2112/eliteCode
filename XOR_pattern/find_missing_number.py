
# Method 2 (Efficient method) : 
# 1- Find the remainder of n by moduling it with 4. 
# 2- If rem = 0, then XOR will be same as n. 
# 3- If rem = 1, then XOR will be 1. 
# 4- If rem = 2, then XOR will be n+1. 
# 5- If rem = 3 ,then XOR will be 0.




# xor 1 with 0 = 1, 
# 0 with 0 = 0,
#  1 with 1 = 0,
#   0 with 1 = 1



def find_missing_number(nums):
	n = len(nums)
	x1 = 1
	for i in range(2, n+1):
		print(i,x1)
		x1 = x1^i
		print('ans -', x1)

	x2 = nums[0]
	for i in range(1, n+1):
		x2 = x2^nums[i]	
	

	# it will return the missing number
	return x1^x2	



def find_single_number(nums):
	x1 = 0
	for i in nums:
		x1^=i

	return x1


print(find_single_number([1,5,1,5,4]))		