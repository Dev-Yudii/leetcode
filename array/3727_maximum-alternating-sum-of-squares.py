"""
This problem was extracted on 2026-10-13 09:46 (UTC-3) from LeetCode at https://leetcode.com/problems/maximum-alternating-sum-of-squares/.
You can check the full problem description there.
Problem Title:
    Maximum Alternating Sum of Squares
Difficulty:
    Medium
Tags:
    Array, Greedy, Sorting
"""

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: nums = [1,2,3]  |  Expected Output: 12
    inputs1 = {}
    exec('nums = [1,2,3]', {}, inputs1)
    print(f'Test 1 Result:', solution.maxAlternatingSum(**inputs1), ' | Expected:', '12')

    # Example Input: nums = [1,-1,2,-2,3,-3]  |  Expected Output: 16
    inputs2 = {}
    exec('nums = [1,-1,2,-2,3,-3]', {}, inputs2)
    print(f'Test 2 Result:', solution.maxAlternatingSum(**inputs2), ' | Expected:', '16')

"""
Notes:
    -
"""
