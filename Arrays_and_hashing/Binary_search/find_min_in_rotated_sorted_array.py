"""Iterative approach"""
def find_min_in_array(s):
    beg, end = 0, len(s) - 1 
    while beg < end:
        mid = (beg + end)//2 
        if s[mid] > s[end]:
            beg = mid + 1 
        else:
            end = mid 
    return s[beg]

nums = [4,5,6,7,0,1,2] 
print(find_min_in_array(nums))

"""Recursive approach"""
class Solution:
    def find(self, beg, end, nums):
        if beg >= end:
            return nums[end]
        mid = (beg + end)//2 
        if nums[mid] > nums[end]:
            return self.find(mid+1, end, nums)
        else:
            return self.find(beg, mid, nums)

    def findMin(self, nums: List[int]) -> int:
        return self.find(0, len(nums)-1, nums)
