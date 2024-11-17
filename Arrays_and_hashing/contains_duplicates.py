class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map_nums = {}
        for number in nums:
            map_nums[number] = 1 + map_nums.get(number, 0)
        for key,value in map_nums.items():
            if value > 1: 
                return True 
        return False 
        