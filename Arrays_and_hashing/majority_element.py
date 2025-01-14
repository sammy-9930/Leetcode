"""
Time complexity: o(n)
Space complexity: o(n)
"""
def find_majority(nums):
    seen = {}
    max_count = 0
    major_element = 0
    for number in nums:
        seen[number] = 1 + seen.get(number, 0)
        if seen[number] > max_count:
            max_count = seen[number]
            major_element = number
    return major_element
    
    
nums = [2, 2, 1, 1, 1, 2, 2]
print(find_majority(nums))

"""
Boyer-Moore Voting Algorithm
Time complexity: o(n)
Space complexity: o(1)
"""
def find_majority(nums):
    count = 0
    candidate = None 
    for number in nums:
        if count == 0:
            candidate = number 
        if candidate == number:
            count += 1 
        else:
            count -= 1 
    return candidate

nums = [2, 2, 1, 1, 1, 2, 2]
print(find_majority(nums))