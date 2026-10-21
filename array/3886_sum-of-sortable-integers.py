"""
This problem was extracted on 2026-10-20 13:14 (UTC-3) from LeetCode at https://leetcode.com/problems/sum-of-sortable-integers/.
You can check the full problem description there.
Problem Title:
    Sum of Sortable Integers
Difficulty:
    Hard
Tags:
    Array, Math, Sorting, Enumeration
"""

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: nums = [3,1,2]  |  Expected Output: 3
    inputs1 = {}
    exec('nums = [3,1,2]', {}, inputs1)
    print(f'Test 1 Result:', solution.sortableIntegers(**inputs1), ' | Expected:', '3')

    # Example Input: nums = [7,6,5]  |  Expected Output: 0
    inputs2 = {}
    exec('nums = [7,6,5]', {}, inputs2)
    print(f'Test 2 Result:', solution.sortableIntegers(**inputs2), ' | Expected:', '0')

    # Example Input: nums = [5,8]  |  Expected Output: 3
    inputs3 = {}
    exec('nums = [5,8]', {}, inputs3)
    print(f'Test 3 Result:', solution.sortableIntegers(**inputs3), ' | Expected:', '3')

"""
Notes:
    -
"""
