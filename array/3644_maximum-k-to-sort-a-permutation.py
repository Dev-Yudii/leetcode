"""
This problem was extracted on 2026-11-04 12:00 (UTC-3) from LeetCode at https://leetcode.com/problems/maximum-k-to-sort-a-permutation/.
You can check the full problem description there.
Problem Title:
    Maximum K to Sort a Permutation
Difficulty:
    Medium
Tags:
    Array, Bit Manipulation
"""

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: nums = [0,3,2,1]  |  Expected Output: 1
    inputs1 = {'nums': [0, 3, 2, 1]}
    print(f'Test 1 Result:', solution.sortPermutation(**inputs1), ' | Expected:', 1)

    # Example Input: nums = [0,1,3,2]  |  Expected Output: 2
    inputs2 = {'nums': [0, 1, 3, 2]}
    print(f'Test 2 Result:', solution.sortPermutation(**inputs2), ' | Expected:', 2)

    # Example Input: nums = [3,2,1,0]  |  Expected Output: 0
    inputs3 = {'nums': [3, 2, 1, 0]}
    print(f'Test 3 Result:', solution.sortPermutation(**inputs3), ' | Expected:', 0)

"""
Notes:
    -
"""
