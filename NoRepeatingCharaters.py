def noRepeatingCharacters(s):
	window_start = 0
	max_length = 0
	chars = {}

	for window_end in range(len(s)):
		if s[window_end] in chars:
			window_start = max(window_start, chars[s[window_end]]+1)
		chars[s[window_end]] = window_end
		max_length = max(max_length, window_end-window_start+1)
	return max_length


s = "aabccbb"
print(noRepeatingCharacters(s))	