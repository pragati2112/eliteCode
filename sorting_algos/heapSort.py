from typing import List


def heapify(nums, n, i):
    largest = i
    left_c = 2 * i + 1
    right_c = 2 * i + 2

    if left_c < n and nums[left_c] > nums[largest]:
        largest = left_c

    if right_c < n and nums[right_c] > nums[largest]:
        largest = right_c

    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)


def heapSort(nums):
    n = len(nums)
    m = n // 2

    for i in range(m, -1, -1):
        # build a max-heap
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        # swap first element and last element of array
        # nums[i] is your last element
        # after swapping it becomes root node

        # then heapify again with root node only

        nums[i], nums[0] = nums[0], nums[i]

        # heapify root element only
        heapify(nums, i, 0)

    return nums


if __name__ == '__main__':
    nums = [8, 7, 2, 1, 0, 9, 6]

    print(heapSort(nums))
