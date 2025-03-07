def merge_strings_alternately(word1, word2):
    res = []
    i, j = 0, 0 
    while i < len(word1) and j < len(word2):
        res.append(word1[i])
        res.append(word2[j])
        i = i + 1 
        j = j + 1
    res.append(word1[i:])
    res.append(word2[j:])
    return ''.join(res)

print(merge_strings_alternately("abc","pqr"))
print(merge_strings_alternately("ab","pqrs"))