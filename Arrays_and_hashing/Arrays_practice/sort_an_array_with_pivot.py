"""
Given any array, consider the last element of an array to be the pivot 
and sort the array with respect to this. 
"""

def partition(arr):
    n = len(arr) - 1 
    pivot = arr[n]
    i = j = 0
    while i < n:
        if arr[i] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1 
        i += 1 
    arr[j], arr[n] = arr[n], arr[j]
    return arr
            
arr = [10, 7, 8, 9, 1, 5]
print(f"Initial array: {arr}")
print(f"Final array: {partition(arr)}")


"""Yet to analyse this part"""
def partition(arr):
    pivot = arr[-1]  # Last element as pivot
    j = 0  # Pointer for the right position of elements less than or equal to pivot
    
    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]  # Swap to ensure smaller elements are on the left
            j += 1
    
    # Place the pivot in the correct position
    arr[j], arr[-1] = arr[-1], arr[j]
    return j  # Return the index of the pivot

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    # Partitioning the array
    pivot_index = partition(arr)
    
    # Recursively sort the sub-arrays
    left = quicksort(arr[:pivot_index])
    right = quicksort(arr[pivot_index + 1:])
    
    # Combine the sorted arrays
    return left + [arr[pivot_index]] + right

# Example Usage
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)
print("Sorted Array:", sorted_arr)
