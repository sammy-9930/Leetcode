import heapq
"""
Sorting 
Time complexity: O(nlogn)
Space complexity: O(n)
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        arr = []
        count = {}
        for number in nums:
            count[number] = 1 + count.get(number, 0)
        for key, value in count.items():
            arr.append([value, key])
        arr.sort(reverse=True)
        for i in range(len(arr)):
            res.append(arr[i][1])
            if len(res) == k:
                return res 

"""
Heapify
Time complexity: O(nlogk)
Space complexity: O(n+k)
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for number in nums:
            count[number] = 1 + count.get(number, 0)
        
        heap = []
        for key,value in count.items():
            heapq.heappush(heap, [value, key])
            # remove least occuring element 
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res 

        
"""
Bucket sort
Time complexity: O(n)
Space complexity: O(n)
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        res = []
        for number in nums:
            count[number] = 1 + count.get(number, 0)
        for key, value in count.items():
            freq[value].append(key)
        for i in range(len(freq) - 1, 0, -1):
            res += freq[i]
            if len(res) == k:
                return res 

"""
res += and res.append() handles input differently 
res = []
res.append(1)        # Adds 1 as an element
print(res)           # Output: [1]

res.append([2, 3])   # Adds the list [2, 3] as a single element
print(res)           # Output: [1, [2, 3]]

res = []
res += [1]          # Extends the list with the elements from [1]
print(res)          # Output: [1]

res += [2, 3]       # Extends the list with the elements from [2, 3]
can be list, tuple etc 
print(res)          # Output: [1, 2, 3]
if something is not iterable, it will raise a type error 
res = []
res += 1  # TypeError: 'int' object is not iterable
"""

        