from typing import List


def bubbleSort(nums: List[int]) -> List:
    for i in range(len(nums)):
        swapped = False

        for j in range(0, len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if swapped == False:  # if already sorted
            break

    return nums


if __name__ == '__main__':
    nums = [20, 3, 4, 1, 22, 45]

    print(bubbleSort(nums))
