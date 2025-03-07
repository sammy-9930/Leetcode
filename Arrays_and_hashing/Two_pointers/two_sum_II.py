from typing import List 

def twoSum(numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1 
        while l < r:
            cur_sum = numbers[l] + numbers[r]
            if cur_sum > target:
                r -= 1 
            elif cur_sum < target:
                l += 1 
            else:
                return [l+1, r+1]
            
numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))
numbers = [2, 3, 6]
target = 6 
print(twoSum(numbers, target))