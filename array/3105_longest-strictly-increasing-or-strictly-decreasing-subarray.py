"""
This problem was extracted on 2026-11-12 08:21 (UTC+0) from LeetCode at https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/.
You can check the full problem description there.
Problem Title:
    Longest Strictly Increasing or Strictly Decreasing Subarray
Difficulty:
    Easy
Tags:
    Array
"""

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Running the examples extracted from the problem statement:")
    print("-" * 40)
    # Example Input: nums = [1,4,3,3,2]  |  Expected Output: 2
    inputs1 = {'nums': [1, 4, 3, 3, 2]}
    print(f'Test 1 Result:', solution.longestMonotonicSubarray(**inputs1), ' | Expected:', 2)

    # Example Input: nums = [3,3,3,3]  |  Expected Output: 1
    inputs2 = {'nums': [3, 3, 3, 3]}
    print(f'Test 2 Result:', solution.longestMonotonicSubarray(**inputs2), ' | Expected:', 1)

    # Example Input: nums = [3,2,1]  |  Expected Output: 3
    inputs3 = {'nums': [3, 2, 1]}
    print(f'Test 3 Result:', solution.longestMonotonicSubarray(**inputs3), ' | Expected:', 3)

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
