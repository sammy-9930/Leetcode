"""Check if an array is a palindrome"""

"""
Brute force 
"""
def func(arr):
    n = len(arr)
    for i in range(n//2):
        if arr[i] != arr[n - i - 1]:
            return False 
    return True 
arr = [3, 6,  6, 3]
print(func(arr))

"""
optimal
"""
def func(arr):
    return arr == arr[::-1]
arr = [1, 2, 3, 4, 5]
print(func(arr))