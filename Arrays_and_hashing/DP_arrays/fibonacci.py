"""
Recursion - top down
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

"""
Iterative approach - bottom up
Time complexity: O(n)
Space complexity: O(n) - only array
"""  
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        res = [-1] * (n+1)
        res[0], res[1] = 0, 1 
        for i in range(2, n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]

"""
Time complexity : O(n)
Space complexity : O(1)

"""     
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n 
        first_val, sec_val = 0, 1 
        for i in range(2, n+1):
            res = first_val + sec_val
            first_val = sec_val
            sec_val = res 
        return res
        