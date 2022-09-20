from typing import List


class Solution:
    def checkPossibility(self, nums: List[int], k: int) -> int:
        low = 0
        high = len(nums) - 1
        # mid = (high + low) // 2

        while low <= high:
            mid = (high + low) // 2

            if k == nums[mid]:
                return mid

            if k > nums[mid]:
                low = mid + 1

            if k < nums[mid]:
                high = mid - 1

        return -1


if __name__ == '__main__':
    nums = [1, 3, 4, 5, 10, 15, 20, 25, 30, 45, 50]

    t = Solution()
    print(t.checkPossibility(nums, 1))
