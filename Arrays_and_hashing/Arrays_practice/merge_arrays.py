"""
Brute force approach
Time complexity = O(m+n)log(m+n)
Space complexity = O(m+n)
"""
def merge_arrays(arr1, arr2):
    res = arr1 + arr2 
    return sorted(res)

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print(merge_arrays(arr1, arr2))

"""
Merge of merge sort
Time complexity:
Space complexity: 
"""
def merge_arrays(arr1, arr2):
    res = []
    len1 = len(arr1) - 1
    len2 = len(arr2) - 1
    i, j = 0, 0
    while i <= len1 and j <= len2:
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1 
        else:
            res.append(arr2[j])
            j += 1
    if j <= len2:
        while j <= len2:
            res.append(arr2[j])
            j += 1
    if i <= len1:
        while i <= len1:
            res.append(arr1[i])
            i += 1
    return res
        

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print(merge_arrays(arr1, arr2))

