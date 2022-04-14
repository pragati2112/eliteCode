from typing import List 

class Solution:
    def mergeSort(self, nums):
        
        if len(nums)<2:
            return nums
        
        middle = len(nums)//2
        left = self.mergeSort(nums[:middle])
        right = self.mergeSort(nums[middle:])
        
        return self.merge(left, right)
    
    
    def merge(self, left, right):
        if not len(left) or not len(right):
            return left or right

        i, j = 0, 0
        result = []
        
        while len(result)< len(left)+len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
            
            if i ==len(left) or j == len(right):
                result.extend(left[i:] or right[j:])
                break
        
        return result
        
        
        
        
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]* nums[i]   
        
        return self.mergeSort(nums)



if __name__ == '__main__':

    t = Solution()

    nums = [2, 1, 3, 7, 8, 5]


    print(t.sortedSquares(nums))        
        