from typing import List


class Solution:

    def sumBetweenTwoNums(self, a, b):
        return ((a + b) * (b - a + 1)) // 2

    def MinimumKMoves(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        nums.append(0)
        nums = sorted(nums)

        print(nums)
        elems = []
        cur_sum = 0

        for i in range(len(nums)):
            if i == len(nums) - 1:
                # elems = elems + [*range(nums[i]+1, nums[i] + 1 + abs(len(elems) - k ))]
                cur_sum += self.sumBetweenTwoNums(nums[i] + 1, nums[i] + k)
                break

            if abs(nums[i] - nums[i + 1]) > 1:
                # elems = elems+[*range(nums[i]+1, nums[i+1])]
                cur_sum += self.sumBetweenTwoNums(nums[i] + 1, nums[i] + min(k, abs(nums[i] - nums[i + 1]) - 1))
                k -= min(abs(nums[i] - nums[i + 1]) - 1, k)

            if k == 0:
                return cur_sum

        return cur_sum

        # return sum(elems[:k])


if __name__ == '__main__':
    # nums = [53,41,90,33,84,26,50,32,63,47,66,43,29,88,71,28,83]
    # nums = [1,2,3,4]

    nums = [20, 83, 66, 95, 76, 36, 44, 40, 21, 93, 83, 51, 8, 26, 96, 42, 4, 64, 63, 72, 18, 80, 25, 27, 22, 68, 27,
            24, 83, 57, 4, 54, 35, 38, 52, 63, 25, 66, 32, 75, 22, 97, 54, 83, 40, 46, 9, 84, 76, 46, 56, 44, 75, 21, 4,
            28, 67, 79, 48, 52, 83, 82, 73, 99, 75, 10, 51, 92, 49, 79, 58, 54, 33, 19, 96, 11, 27, 48, 42, 6, 27, 96,
            7, 26, 26, 50, 97, 83, 14]

    t = Solution()
    print(t.MinimumKMoves(nums, 24))
