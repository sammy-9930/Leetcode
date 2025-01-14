# [1, 2, 3]
# [6, 3, 2]
def product_of_array_except_self(arr):
    res = 1
    zero_count = 0
    for number in nums:
        if number != 0:
            res *= number 
        else:
            zero_count += 1 
    if zero_count > 1:
        return [0]*len(nums)
    for i in range(len(nums)):
        if nums[i] != 0 and zero_count == 1:
            nums[i] = 0 
        elif nums[i] == 0 and zero_count == 1:
            nums[i] = res 
        else:
            nums[i] = res // nums[i]
    return nums

        
nums = [-1,1,0,-3,3]
print(product_of_array_except_self(nums))
