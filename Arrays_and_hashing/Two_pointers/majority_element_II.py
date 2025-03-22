from typing import List

"""
Using hashmap 
Time complexity: O(n)
Space complexity: O(n)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        seen = {}
        for number in nums:
            seen[number] = 1 + seen.get(number, 0)
            if seen[number] > len(nums)//3 and number not in res:
                res.append(number)
        return res
    
"""
Time complexity: O(n)
Space complexity: O(1)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        # find candidates 
        candidate1 = None 
        candidate2 = None 
        count1, count2 = 0, 0
        for number in nums:
            if number == candidate1:
                count1 += 1 
            elif number == candidate2:
                count2 += 1 
            elif count1 == 0:
                candidate1, count1 = number, 1 
            elif count2 == 0:
                candidate2, count2 = number, 1 
            else:
                count1 -= 1 
                count2 -= 1 
        # verify candidates 
        result = []
        if nums.count(candidate1) > len(nums)//3:
            result.append(candidate1)
        if candidate2 != candidate1 and nums.count(candidate2) > len(nums)//3:
            result.append(candidate2)
        return result
