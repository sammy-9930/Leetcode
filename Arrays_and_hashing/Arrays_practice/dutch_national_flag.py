class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1 
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1 
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        print(nums)
        return nums 


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c0 = 0
        c1 = 0
        c2 = 0
        for number in nums:
            if number == 0:
                c0 += 1
            elif number == 1:
                c1 += 1
            else:
                c2 += 1
        for i in range(c0):
            nums[i] = 0
            
        for i in range(c1):
            nums[i + c0] = 1
             
        for i in range(c2):
            nums[i + c0 + c1] = 2
           
        print(nums)
        return nums
        


        