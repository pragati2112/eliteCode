def mins_substr(s, t):
    if len(s) < len(t):
        return ""

    t_map = {}
    s_map = {}

    for i in range(len(t)):
        char = t[i]
        if char not in t_map:
            t_map[char] = 1
        else:
            t_map[char] += 1

    # char = s[i]
    # if char not in s_map:
    # 	s_map[char] = 1
    # else:
    # 	s_map[char] += 1

    start, end = -1, -1
    for i in range(len(s)):
        if s[i] in t_map:
