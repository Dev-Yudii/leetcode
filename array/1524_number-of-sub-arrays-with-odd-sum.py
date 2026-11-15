"""
This problem was extracted on 2026-11-15 07:52 (UTC+0) from LeetCode at https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/.
You can check the full problem description there.
Problem Title:
    Number of Sub-arrays With Odd Sum
Difficulty:
    Medium
Tags:
    Array, Math, Dynamic Programming, Prefix Sum
"""

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Running the examples extracted from the problem statement:")
    print("-" * 40)
    # Example Input: arr = [1,3,5]  |  Expected Output: 4
    inputs1 = {'arr': [1, 3, 5]}
    print(f'Test 1 Result:', solution.numOfSubarrays(**inputs1), ' | Expected:', 4)

    # Example Input: arr = [2,4,6]  |  Expected Output: 0
    inputs2 = {'arr': [2, 4, 6]}
    print(f'Test 2 Result:', solution.numOfSubarrays(**inputs2), ' | Expected:', 0)

    # Example Input: arr = [1,2,3,4,5,6,7]  |  Expected Output: 16
    inputs3 = {'arr': [1, 2, 3, 4, 5, 6, 7]}
    print(f'Test 3 Result:', solution.numOfSubarrays(**inputs3), ' | Expected:', 16)

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
