import heapq

"""
Brute force 
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
Time complexity: O(nlogk)
Space complexity: O(k)
"""

def k_largest(arr, k):
    max_heap = []
    for number in arr:
        heapq.heappush(max_heap, number)
    while len(max_heap) > k:
        heapq.heappop(max_heap)
    return max_heap[0]

# ALTERNATE 
# def findKthLargest(self, nums, k):
#         return heapq.nlargest(k, nums)[-1]
    
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(k_largest(arr, k))

