"""Brute force"""
def three_sum(arr):
    res = []
    n = len(arr)
    for i in range(n - 2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplet = sorted([arr[i], arr[j], arr[k]])  # Sort the triplet
                    if triplet not in res:  # Avoid duplicates
                        res.append(triplet)
    return res
                    
arr = nums = [-1,0,1,2,-1,-4]
print(three_sum(arr))

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
