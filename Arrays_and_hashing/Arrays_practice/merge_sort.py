def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    # Find the middle point
    mid = len(arr) // 2

    # Divide the array elements into 2 halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    # Merge the two halves into a single sorted list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# Example usage
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)




def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge(left_half)
        merge(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1 
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1 
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        return arr 

arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array: ", arr)
sorted_array = merge(arr)
print("Sorted array: ", sorted_array)