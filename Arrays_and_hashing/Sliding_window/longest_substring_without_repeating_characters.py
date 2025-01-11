"""
Brute force 
time complexity: o(n^2)
space complexity: o(m) m-unique elements in the string
"""
def longest_substring(s):
    res = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            res = max(res, len(seen))
    return res

s = "Hello World!"
print(longest_substring(s))

"""
sliding window: 
time complexity: o(n) n-length of string
space complexity: o(m) m-total unique characters in the string
"""

def longest_substring(s):
    l = 0
    max_length = 0
    seen = set()
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1 
        seen.add(s[r])
        max_length = max(max_length, r - l + 1)
    return max_length

s = "Hello World!"
print(longest_substring(s))
