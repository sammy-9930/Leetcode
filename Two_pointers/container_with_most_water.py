"""Brute force solution"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                b = j - i 
                l = min(height[i], height[j])
                area = l * b 
                # print("height[i]: {height[i]} ,height[j]: {height[j]}")
                # print("length: {l}, breadth: {b}, area: {area}")
                max_area = max(max_area, area)
        return max_area
    
"""Optimized solution"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        beg, end = 0, len(height) - 1 
        max_area = 0
        while beg < end:
            length = min(height[beg], height[end])
            breadth = end - beg 
            area = length * breadth 
            max_area = max(area, max_area)
            if height[beg] <= height[end]:
                beg += 1
            else:
                end -= 1
        return max_area 

        

        