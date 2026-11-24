"""
This problem was extracted on 2026-11-24 10:55 (UTC+0) from LeetCode at https://leetcode.com/problems/maximum-subarray-with-equal-products/.
You can check the full problem description there.
Problem Title:
    Maximum Subarray With Equal Products
Difficulty:
    Easy
Tags:
    Array, Math, Sliding Window, Enumeration, Number Theory
"""

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Running the examples extracted from the problem statement:")
    print("-" * 40)
    # Example Input: nums = [1,2,1,2,1,1,1]  |  Expected Output: 5
    inputs1 = {'nums': [1, 2, 1, 2, 1, 1, 1]}
    print(f'Test 1 Result:', solution.maxLength(**inputs1), ' | Expected:', 5)

    # Example Input: nums = [2,3,4,5,6]  |  Expected Output: 3
    inputs2 = {'nums': [2, 3, 4, 5, 6]}
    print(f'Test 2 Result:', solution.maxLength(**inputs2), ' | Expected:', 3)

    # Example Input: nums = [1,2,3,1,4,5,1]  |  Expected Output: 5
    inputs3 = {'nums': [1, 2, 3, 1, 4, 5, 1]}
    print(f'Test 3 Result:', solution.maxLength(**inputs3), ' | Expected:', 5)

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
