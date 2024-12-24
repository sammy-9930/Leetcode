import heapq
def k_largest(arr, k):
    max_heap = []
    for number in arr:
        heapq.heappush(max_heap, number)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return max_heap[0]
    

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(k_largest(arr, k))