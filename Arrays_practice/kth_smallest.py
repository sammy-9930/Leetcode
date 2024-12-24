def k_smallest(arr, k):
    arr = sorted(arr)
    return arr[k-1]

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(k_smallest(arr, k))

import heapq
def k_smallest(arr, k):
    max_heap = []
    for number in arr:
        heapq.heappush(max_heap, -number)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return -max_heap[0]
    

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(k_smallest(arr, k))