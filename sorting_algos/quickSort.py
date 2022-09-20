from typing import List


def partition(nums, low, high):
    pivot = nums[high]  # rightmost element
    store_idx = low - 1  # keep it at -1, means assume it (leftmost element)

    for i in range(low, high):
        if nums[i] <= pivot:
            store_idx += 1  # while swapping always consider store_idx+=1

            nums[store_idx], nums[i] = nums[i], nums[store_idx]  # then swap

    nums[store_idx + 1], nums[high] = nums[high], nums[
        store_idx + 1]  # swap pivot after traversing the whole partition from low to high

    # then return the new position of pivot after pivot swap
    return store_idx + 1


def quickSort(nums, low, high):
    if low < high:
        pivot_idx = partition(nums, low, high)  # new partition
        quickSort(nums, low, pivot_idx - 1)  # call recursively quicksort on new partition
        quickSort(nums, pivot_idx + 1, high)
    return nums


if __name__ == '__main__':
    nums = [8, 7, 2, 1, 0, 9, 6]

    print(quickSort(nums, 0, len(nums) - 1))
