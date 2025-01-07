def three_sum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
        if i != 0 and nums[i] == nums[i-1]:
            continue 
        l = i + 1 
        r = len(nums) - 1 
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l += 1 
            elif total > 0:
                r -= 1 
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1 
                while l < r and nums[l] == nums[l-1]:
                    l += 1
    return res 
    

arr = [-1,0,1,2,-1,-4]
print(three_sum(arr))