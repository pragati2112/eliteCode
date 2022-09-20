def comparingStrings(s1, s2):
    s1_back_count = s1.count('#')
    s2_back_count = s2.count('#')

    new_s1 = s1
    new_s2 = s2

    print(s2_back_count)

    for i in range(s1_back_count):
        back_index = new_s1.index('#')
        char1 = new_s1[back_index - 1]
        char2 = new_s1[back_index]
        new_s1 = new_s1.replace(char1, '', 1).replace(char2, '', 1)

    for j in range(s2_back_count):
        back_index = new_s2.index('#')
        char1 = new_s2[back_index - 1]
        char2 = new_s2[back_index]
        new_s2 = new_s2.replace(char1, '', 1).replace(char2, '', 1)

    print(new_s1, new_s2)
    return new_s2 == new_s1


str1 = "xp#"
str2 = "xyz##"

print(comparingStrings(str1, str2))
