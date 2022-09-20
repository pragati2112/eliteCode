def wordsConcatenation(s, words):
    window_start = 0
    chars = {}
    result_indexes = []
    word_length = len(words[0])

    k = len(words) * len(words[0])

    for w in words:
        if w not in chars:
            chars[w] = 1
        else:
            chars[w] += 1

    for i in range(len(s) - k + 1):
        word_seen = {}
        for j in range(len(words)):
            next_word_index = i + j * word_length
            word = s[next_word_index:next_word_index + word_length]
            if word not in chars:
                break

            if word not in word_seen:
                word_seen[word] = 1
            else:
                word_seen[word] += 1

            if word_seen[word] > chars.get(word, 0):
                break

            if word_seen == chars:
                result_indexes.append(i)

    return result_indexes


string = "catcatfoxfox"
words = ["cat", "fox"]
print(wordsConcatenation(string, words))
