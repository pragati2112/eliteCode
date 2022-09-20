# Given a string with lowercase letters only, 
# if you are allowed to replace no more than ‘k’ letters with any letter,
# find the length of the longest substring having the same letters after replacement.


def longestSubString(k, s):
    window_start = 0
    max_length = 0
    chars = {}
    char_max_frequency = 0

    for i in range(len(s)):
        if s[i] not in chars:
            chars[s[i]] = 0

        chars[s[i]] += 1
        char_max_frequency = max(char_max_frequency, chars[s[i]])

        # if unique characters are more than k in window then shrink the window size
        if (i - window_start + 1 - char_max_frequency) > k:
            chars[s[window_start]] -= 1
            window_start += 1

        max_length = max(max_length, i - window_start + 1)
    return max_length


s = 'araaci'
k = 2
print(longestSubString(k, s))
