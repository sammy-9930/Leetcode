class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        for number in num_set:
            # check if we are at the beginning of a sequence 
            # if number before doesn't exist, we are at the beginning of a sequence 
            if number-1 not in num_set:
                cur_num = number 
                cur_len = 1 
                while cur_num+1 in num_set:
                    cur_num += 1 
                    cur_len += 1 
                max_length = max(cur_len, max_length)
        return max_length