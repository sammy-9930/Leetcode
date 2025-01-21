"""
Recursion 
Time complexity: O(2^n)
Space complexity: O(n)
"""
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n 
        return self.fib(n-1) + self.fib(n-2)
    
"""
Recursion with memoization 
Time complexity: O(n) [storing n elements in array]
Space complexity: O(n) + O(n) = O(n) [stack + array]
"""
class Solution(object):
    def helper(self, n_value, arr):
        if n_value <= 1:
            return n_value 
        if arr[n_value] == -1:
            arr[n_value] = self.helper(n_value-1, arr) + self.helper(n_value-2, arr)
        return arr[n_value]

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n 
        values = [-1] * (n+1)
        return self.helper(n, values)

        