def anagramsOfAString(s, p):
    window_start = 0
    chars = {}
    min_len = len(s) + 1
    matched, sub_start = 0, 0

    for i in range(len(p)):
        if p[i] not in chars:
            chars[p[i]] = 1
        else:
            chars[p[i]] += 1

    for window_end in range(len(s)):
        right_char = s[window_end]

        if right_char in chars:
            chars[right_char] -= 1
            if chars[right_char] >= 0:
                matched += 1

        while matched == len(p):
            if min_len > window_end - window_start + 1:
                min_len = window_end - window_start + 1
                sub_start = window_start

            left_char = s[window_start]
            window_start += 1
            if left_char in chars:
                if chars[left_char] == 0:
                    matched -= 1
                chars[left_char] += 1

    if min_len > len(s):
        return ''
    return s[sub_start: sub_start + min_len]


s = "ppqp"
p = "pq"
print(anagramsOfAString(s, p))
