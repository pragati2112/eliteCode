def anagramsOfAString(s, p):
    window_start = 0
    chars = {}
    result_indexes = []
    matched = 0

    for i in range(len(p)):
        if p[i] not in chars:
            chars[p[i]] = 1
        else:
            chars[p[i]] += 1

    for window_end in range(len(s)):
        right_char = s[window_end]

        if right_char in chars:
            chars[right_char] -= 1

            if chars[right_char] == 0:
                matched += 1

        if matched == len(chars):
            result_indexes.append(window_start)

        if window_end >= len(p) - 1:
            left_char = s[window_start]
            window_start += 1
            if left_char in chars:
                if chars[left_char] == 0:
                    matched -= 1
                chars[left_char] += 1

    return result_indexes


s = "ppqp"
p = "pq"
print(anagramsOfAString(s, p))
