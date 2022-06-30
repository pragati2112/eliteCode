def permutationInAString(s, p):

	window_start = 0
	chars = {}
	matched = 0

	#On2 time complexity not good----

	# for i in range(len(p)):
	# 	if p[i] not in chars:
	# 		chars[p[i]] = 1
	# 	else:
	# 		chars[p[i]] +=1


	# k = len(p)
	# for window_end in range(len(s)-k+1):
	# 	sub_str = s[window_end: k]
	# 	sub_chars = {}
	# 	for j in range(len(sub_str)):
	# 		if sub_str[j] not in sub_chars:
	# 			sub_chars[sub_str[j]] = 1
	# 		else:
	# 			sub_chars[sub_str[j]] +=1

	# 	if sub_chars == chars:
	# 		return True

	# 	k += 1

	# return False


	for i in range(len(p)):
		if p[i] not in chars:
			chars[p[i]] = 1
		else:
			chars[p[i]] +=1


	for window_end in range(len(s)):
		right_char = s[window_end]

		if right_char in chars:
			chars[right_char] -=1

			if chars[right_char] == 0:
				matched+=1

		if matched == len(chars):
			return True

		if window_end >=len(p)-1:
			left_char = s[window_start]
			window_start+=1
			if left_char in chars:
				if chars[left_char] == 0:
					matched-=1
				chars[left_char] +=1

	return False

s="odicf"
p="dc"
print(permutationInAString(s, p))	