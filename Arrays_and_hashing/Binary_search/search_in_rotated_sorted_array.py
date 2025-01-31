def search_in_rotated_sorted_array(arr, target):
    low, high = 0, len(arr) - 1 
    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid 
        
        if nums[low] < nums[mid]:
            if nums[low] <= target <= nums[high]:
                high = mid - 1 
            else:
                low = mid + 1 
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1 
            else:
                high = mid - 1 
    return -1 


nums = [4,5,6,7,0,1,2]
target = 0
print(search_in_rotated_sorted_array(nums, target))
