"""
This problem was extracted on 2026-11-05 11:14 (UTC+0) from LeetCode at https://leetcode.com/problems/smallest-stable-index-ii/.
You can check the full problem description there.
Problem Title:
    Smallest Stable Index II
Difficulty:
    Medium
Tags:
    Array, Prefix Sum
"""

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: nums = [5,0,1,4], k = 3  |  Expected Output: 3
    inputs1 = {'nums': [5, 0, 1, 4], 'k': 3}
    print(f'Test 1 Result:', solution.firstStableIndex(**inputs1), ' | Expected:', 3)

    # Example Input: nums = [3,2,1], k = 1  |  Expected Output: -1
    inputs2 = {'nums': [3, 2, 1], 'k': 1}
    print(f'Test 2 Result:', solution.firstStableIndex(**inputs2), ' | Expected:', -1)

    # Example Input: nums = [0], k = 0  |  Expected Output: 0
    inputs3 = {'nums': [0], 'k': 0}
    print(f'Test 3 Result:', solution.firstStableIndex(**inputs3), ' | Expected:', 0)

"""
Notes:
    -
"""
