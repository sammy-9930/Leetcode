from typing import List
"""
Iterative approach
Time complexity: O(n^4) worst case 
Space complexity : O(n^4) storing all possible combinations
"""
def letter_combinations(digits):
    if digits == "":
            return []
    combinations = [""]
    number_map = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
    }
    for digit in digits:
        new_combination = []
        for combo in combinations:
            for char in number_map[digit]:
                new_combination.append(combo+char)
        combinations = new_combination
    return combinations

"""
Backtracking 
Time complexity: O(n^4) 
Space complexity : O(n^4)
"""
def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        combinations = []
        number_map = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        def backtrack(ind, new_combination):
            if ind == len(digits):
                combinations.append(new_combination)
                return 
            for c in number_map[digits[ind]]:
                backtrack(ind+1, new_combination+c)
        backtrack(0, "")

        return combinations

print(letter_combinations("23"))