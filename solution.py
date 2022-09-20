class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        fault_count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                fault_count += 1
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]

        return fault_count <= 1
