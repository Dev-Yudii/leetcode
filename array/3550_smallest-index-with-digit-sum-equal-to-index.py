"""
This problem was extracted on 2026-11-05 11:21 (UTC+0) from LeetCode at https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/.
You can check the full problem description there.
Problem Title:
    Smallest Index With Digit Sum Equal to Index
Difficulty:
    Easy
Tags:
    Array, Math
"""

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: nums = [1,3,2]  |  Expected Output: 2
    inputs1 = {'nums': [1, 3, 2]}
    print(f'Test 1 Result:', solution.smallestIndex(**inputs1), ' | Expected:', 2)

    # Example Input: nums = [1,10,11]  |  Expected Output: 1
    inputs2 = {'nums': [1, 10, 11]}
    print(f'Test 2 Result:', solution.smallestIndex(**inputs2), ' | Expected:', 1)

    # Example Input: nums = [1,2,3]  |  Expected Output: -1
    inputs3 = {'nums': [1, 2, 3]}
    print(f'Test 3 Result:', solution.smallestIndex(**inputs3), ' | Expected:', -1)

"""
Notes:
    -
"""
