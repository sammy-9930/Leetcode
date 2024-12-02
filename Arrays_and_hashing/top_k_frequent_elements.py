class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq = [[] for i in range(len(nums)+ 1)]
        for number in nums:
            count[number] = 1 + count.get(number, 0)
        for key,value in count.items():
            freq[value].append(key)
        res = []
        print(len(freq))
        print(freq)
        for i in range(len(freq)-1, 0, -1):
            # append individual elements 
            res += freq[i]
            if len(res) == k:
                return res 