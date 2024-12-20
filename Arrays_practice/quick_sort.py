"""
Quick sort 
Time complexity:
Best and average case : pivot element divides array into 2 equal part :O(nlogn)
worst case: the pivot is the smallest or largest element in the array: O(n2)

Space complexity:
Best and average case: O(logn)
Worst case: O(n) 
"""
def quicksort(arr):
    if len(arr) <= 1:
        return arr 
    pivot = arr[0]
    left = [element for element in arr if element < pivot]
    right = [element for element in arr if element >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

arr = [1, 7, 4, 1, 10, 9, -2]
print(quicksort(arr))

"""
choosing last element as pivot
"""
def quicksort(arr):
    if len(arr) <= 1:
        return arr 
    pivot = arr[-1]
    left = [element for element in arr[:-1] if element < pivot]
    right = [element for element in arr[:-1] if element >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

arr = [1, 7, 4, 1, 10, 9, -2]
print(quicksort(arr))

"""
Middle element as pivot
"""    
def quicksort(arr):
    if len(arr) <= 1:
        return arr 
    pivot = arr[len(arr) // 2]
    left = [element for element in arr if element < pivot and element != pivot]
    right = [element for element in arr if element > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

arr = [1, 7, 4, 1, 10, 9, -2]
print(quicksort(arr))