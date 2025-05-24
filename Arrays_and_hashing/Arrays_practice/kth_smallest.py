def k_smallest(arr, k):
    arr = sorted(arr)
    return arr[k-1]

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(k_smallest(arr, k))

import heapq
def k_smallest(arr, k):
    heapq.heapify(arr)
    for _ in range(k-1):
        heapq.heappop(arr)
    return heapq.heappop(arr)
    

arr = [7, 10, 4, 3, 20, 15]
k = 5
print(k_smallest(arr, k))