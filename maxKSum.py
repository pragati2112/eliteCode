from typing import List


class Solution:
	def checkPossibility(self, nums: List[int], k: int) -> int:
		nums = nums*k

		# lists = [[]]
		# for i in range(len(nums) + 1):
		# 	for j in range(i):
		# 		lists.append(nums[j: i])	

		ans = nums[0]
		subarr_sum = nums[0] 

		for i in range(1, len(nums)):
			subarr_sum = max(nums[i], nums[i] + subarr_sum)
			ans = max(ans, subarr_sum)
		return ans		 		





if __name__ == '__main__':

  nums = [1, -2, 1]

  t = Solution()
  print(t.checkPossibility(nums, 5))
