'''
Write a function best_sum(nums, target) 
It should return an array containing any combinations of elements that add up to exactly the target.
If there are many arrays return the shortest array. ie array with smallest length
If there is no such array, return None

you can use any element as many times (Repetition allowed )

'''


def best_sum(arr, target):
    if len(arr) == 1 and arr[0] == target:
        return arr

    if target == 0: return []

    if target < 0: return None
    result = None

    for i in range(len(arr)):
        new_target = target - arr[i]
        temp = best_sum(arr, new_target)
        if temp is not None:
            ans_tmp = [*temp, arr[i]]
            if result is None or len(result) > len(ans_tmp):
                result = ans_tmp
    return result


# print(best_sum(target = 50,arr = [2,5,8,25]))


# ===================================================================


hash_map = {}


def best_sum_dp(arr, target):
    # if len(arr)==1 and arr[0]==target:
    # 	return arr

    if target in hash_map.keys():
        return hash_map[target]

    if target == 0: return []

    if target < 0: return None
    result = None

    for i in range(len(arr)):
        new_target = target - arr[i]
        temp = best_sum_dp(arr, new_target)
        if temp is not None:
            ans_tmp = [*temp, arr[i]]
            if result is None or len(result) >= len(ans_tmp):
                result = ans_tmp
            # print('***',result)

    hash_map[target] = result
    return result


print(best_sum_dp(target=50, arr=[1, 2, 3, 25]))
