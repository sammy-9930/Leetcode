import heapq

"""
Brute force - using built-in sort 
Time complexity: O(nlogn)
Space complexity: O(1)
"""
def k_largest(arr, k):
    arr.sort()
    return arr[len(arr) - k]

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(k_largest(arr, k))

"""
Min heap 
Time complexity: O(n + klogn)
O(n) - time to create heap, O(klogn)- adjust the elements assuming k << n 
Space complexity: O(1) modifying nums in place 
"""

def k_largest(nums, k):
    for i in range(len(nums)):
        nums[i] = -nums[i]

    heapq.heapify(nums)

    for _ in range(k-1):
        heapq.heappop(nums)

    return -1 * heapq.heappop(nums)
    
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(k_largest(arr, k))

"""
heapq.heapify by default creates a min-heap in python. 
"""