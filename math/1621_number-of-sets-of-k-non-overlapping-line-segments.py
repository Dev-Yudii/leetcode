"""
This problem was extracted on 2026-11-05 11:18 (UTC+0) from LeetCode at https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/.
You can check the full problem description there.
Problem Title:
    Number of Sets of K Non-Overlapping Line Segments
Difficulty:
    Medium
Tags:
    Math, Dynamic Programming, Combinatorics, Prefix Sum
"""

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: n = 4, k = 2  |  Expected Output: 5
    inputs1 = {'n': 4, 'k': 2}
    print(f'Test 1 Result:', solution.numberOfSets(**inputs1), ' | Expected:', 5)

    # Example Input: n = 3, k = 1  |  Expected Output: 3
    inputs2 = {'n': 3, 'k': 1}
    print(f'Test 2 Result:', solution.numberOfSets(**inputs2), ' | Expected:', 3)

    # Example Input: n = 30, k = 7  |  Expected Output: 796297179
    inputs3 = {'n': 30, 'k': 7}
    print(f'Test 3 Result:', solution.numberOfSets(**inputs3), ' | Expected:', 796297179)

"""
Notes:
    -
"""
