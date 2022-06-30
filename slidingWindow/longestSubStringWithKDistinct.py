def longestSubStringWithKDistinct(k, s):
	window_start = 0
	max_length = 0
	chars = {}

	for i in range(len(s)):
		if s[i] not in chars:
			chars[s[i]] = 1
		else:
			chars[s[i]] +=1	

		while len(chars) > k:
			chars[s[window_start]] -=1
			if chars[s[window_start]] == 0:
				del chars[s[window_start]]
			window_start +=1

		max_length = max(max_length, i-window_start+1)
	return max_length




s = 'araaci'
k = 2
print(longestSubStringWithKDistinct(k, s))	