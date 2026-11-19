"""
This problem was extracted on 2026-11-19 08:49 (UTC+0) from LeetCode at https://leetcode.com/problems/minimum-score-by-changing-two-elements/.
You can check the full problem description there.
Problem Title:
    Minimum Score by Changing Two Elements
Difficulty:
    Medium
Tags:
    Array, Greedy, Sorting
"""

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Running the examples extracted from the problem statement:")
    print("-" * 40)
    # Example Input: nums = [1,4,7,8,5]  |  Expected Output: 3
    inputs1 = {'nums': [1, 4, 7, 8, 5]}
    print(f'Test 1 Result:', solution.minimizeSum(**inputs1), ' | Expected:', 3)

    # Example Input: nums = [1,4,3]  |  Expected Output: 0
    inputs2 = {'nums': [1, 4, 3]}
    print(f'Test 2 Result:', solution.minimizeSum(**inputs2), ' | Expected:', 0)

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
