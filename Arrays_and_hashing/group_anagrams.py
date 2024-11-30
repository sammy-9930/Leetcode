from collections import defaultdict

"""
sorting
time complexity: O(m∗nlogn)
space complexity: O(m∗n)
m is the number of strings and n is the length of the longest string 
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            res[sorted_s].append(s)
        return res.values()
        

"""
Hashtable implementation
time complexity: O(m∗n)
space complexity: O(m)
where m is the number of strings and n is the length of the longest string. 
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        print(res)
        for s in strs:
            count = [0] * 26 
            for char in s:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(s)
        return res.values()
    """
    POINTERS FOR THIS PROBLEM:
     final result 
        key cannot be list so convert to tuple 
        {
        (1, 0, 1, ...): ["eat", "tea", "ate"],
        (1, 0, 0, 1, ...): ["tan", "nat"],
        (1, 1, 0, 0, ...): ["bat"]
        }
    - the default value of key in a defaultdict is [] if we use defaultdict(list). 0 if we use defaultdict(int)
    - defaultdict is designed to store lists as values.
    - If you assign res['new_key'] = 'value', you replace the entire list for that key with a single string ('value').
    - This defeats the purpose of using defaultdict(list), as it is specifically meant to store lists of values.
    """    
