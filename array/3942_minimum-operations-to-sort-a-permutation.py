"""
This problem was extracted on 2026-10-22 14:28 (UTC-3) from LeetCode at https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/.
You can check the full problem description there.
Problem Title:
    Minimum Operations to Sort a Permutation
Difficulty:
    Medium
Tags:
    Array
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: nums = [0,2,1]  |  Expected Output: 2
    inputs1 = {'nums': [0, 2, 1]}
    print(f'Test 1 Result:', solution.minOperations(**inputs1), ' | Expected:', 2)

    # Example Input: nums = [1,0,2]  |  Expected Output: 2
    inputs2 = {'nums': [1, 0, 2]}
    print(f'Test 2 Result:', solution.minOperations(**inputs2), ' | Expected:', 2)

    # Example Input: nums = [2,0,1,3]  |  Expected Output: -1
    inputs3 = {'nums': [2, 0, 1, 3]}
    print(f'Test 3 Result:', solution.minOperations(**inputs3), ' | Expected:', -1)

"""
Notes:
    -
"""
