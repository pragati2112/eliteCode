def longestSubString(k, arr):
	window_start = 0
	max_length = 0
	ones_count = 0

	for i in range(len(arr)):
		if arr[i]==1:
			ones_count +=1	

		if(i-window_start+1-ones_count)>k:
			if arr[window_start] == 1:
				ones_count -=1
			window_start +=1

		max_length = max(max_length, i-window_start+1)
	return max_length




arr=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k=2
print(longestSubString(k, arr))	