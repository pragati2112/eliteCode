def lengthOfLongestSubstring(string):
    """
    :type s: str
    :rtype: int
    """
    ans = 0
    sub = ''
    for char in s:
        if char not in sub:
            sub += char
            ans = max(ans, len(sub))
        else:
            cut = sub.index(char)
            sub = sub[cut + 1:] + char

    print(sub)
    return ans


    # dictionary = {}
    # sub_pos=0

    #         for i in range(0,len(s)):

    #             if s[i] not in dictionary.values():
    #                 dictionary[i] = s[i]

    #             else:
    #                 idx = s.index(s[i])
    #                 print(idx)

    #                 dictionary.pop(idx, s[i])

    print(dictionary)



# your_string_list = list(string)

# sub_string=''
# sub_string_temp=''

# for i in range(len(your_string_list)):

#     if your_string_list[i] in sub_string_temp :
#         if len(sub_string_temp) > len(sub_string):
#             sub_string = sub_string_temp
#             sub_string_temp = ''
#         else:
#             pass
#     else:
#         sub_string_temp = sub_string_temp + your_string_list[i]


# print(sub_string)
# print(sub_string_temp)
# if len(sub_string) > len(sub_string_temp):
#     return len(sub_string)
# else:
#     return len(sub_string_temp)


s = "xzquxpppab"

print(lengthOfLongestSubstring(s))
