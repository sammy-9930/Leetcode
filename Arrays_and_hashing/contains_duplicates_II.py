from typing import List 

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                diff = i - seen[nums[i]]
                if diff <= k:
                    return True 
            seen[nums[i]] = i
        return False 