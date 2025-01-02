# [1, 2, 3]
# [6, 3, 2]
def product_of_array_except_self(arr):
    zero_count = 0
    res = 1 
    for number in arr:
        if number != 0:
            res *= number
        else:
            zero_count += 1 
    for i in range(len(nums)):
        if zero_count > 1:
            return [0] * len(nums)
        if nums[i] == 0:
            nums[i] = res 
        else:
            nums[i] = 0 if zero_count == 1 else res//nums[i] 
    return nums 
        
nums = [-1,1,0,-3,3]
print(product_of_array_except_self(nums))
