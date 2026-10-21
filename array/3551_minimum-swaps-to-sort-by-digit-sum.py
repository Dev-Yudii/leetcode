"""
This problem was extracted on 2026-10-17 20:51 (UTC-3) from LeetCode at https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/.
You can check the full problem description there.
Problem Title:
    Minimum Swaps to Sort by Digit Sum
Difficulty:
    Medium
Tags:
    Array, Hash Table, Sorting
"""

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: nums = [37,100]  |  Expected Output: 1
    inputs1 = {}
    exec('nums = [37,100]', {}, inputs1)
    print(f'Test 1 Result:', solution.minSwaps(**inputs1), ' | Expected:', '1')

    # Example Input: nums = [22,14,33,7]  |  Expected Output: 0
    inputs2 = {}
    exec('nums = [22,14,33,7]', {}, inputs2)
    print(f'Test 2 Result:', solution.minSwaps(**inputs2), ' | Expected:', '0')

    # Example Input: nums = [18,43,34,16]  |  Expected Output: 2
    inputs3 = {}
    exec('nums = [18,43,34,16]', {}, inputs3)
    print(f'Test 3 Result:', solution.minSwaps(**inputs3), ' | Expected:', '2')

"""
Notes:
    -
"""
