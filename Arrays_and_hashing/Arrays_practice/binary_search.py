"""
Iterative binary search
Time complexity : O(logn)
Space complexity: O(n)
"""
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high)//2
        if target == arr[mid]:
            return mid 
        elif target < arr[mid]:
            high = mid - 1 
        else:
            low = mid + 1

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
print(binary_search(arr, target))

"""
Recursive binary search
Time Complexity: O(logn)
Space Complexity: O(logn)

"""
def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low+high) // 2
    if target == arr[mid]:
        return mid 
    elif target < arr[mid]:
        return binary_search(arr, target, low, mid-1)
    else:
        return binary_search(arr, target, mid+1, high)

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
print(binary_search(arr, target, 0, len(arr) - 1))

