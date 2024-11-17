"""
Brute force approach 
time complexity: O(n2)
space complexity: O(1)
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True 
        return False 


"""
Hash Map implementation
time complexity: O(n)
space complexity: O(n)
"""
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
        

"""
Hash set implementation
time complexity: O(n)
space complexity: O(n)
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for number in nums:
            if number in seen:
                return True 
            seen.add(number)
        return False


"""
Sorting 
time complexity: O(nlogn)
space complexity: O(1) or O(n) depending on sorting algorithm
"""        
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True 
        return False 