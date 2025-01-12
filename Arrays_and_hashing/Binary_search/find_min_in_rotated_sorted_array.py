def find_min_in_array(s):
    beg, end = 0, len(s) - 1 
    while beg < end:
        mid = (beg + end)//2 
        if s[mid] > s[end]:
            beg = mid + 1 
        else:
            end = mid 
    return s[beg]

nums = [4,5,6,7,0,1,2] 
print(find_min_in_array(nums))