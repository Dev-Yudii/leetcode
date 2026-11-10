"""
This problem was extracted on 2026-11-10 08:26 (UTC+0) from LeetCode at https://leetcode.com/problems/climbing-stairs-ii/.
You can check the full problem description there.
Problem Title:
    Climbing Stairs II
Difficulty:
    Medium
Tags:
    Array, Dynamic Programming
"""

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Running the examples extracted from the problem statement:")
    print("-" * 40)
    # Example Input: n = 4, costs = [1,2,3,4]  |  Expected Output: 13
    inputs1 = {'n': 4, 'costs': [1, 2, 3, 4]}
    print(f'Test 1 Result:', solution.climbStairs(**inputs1), ' | Expected:', 13)

    # Example Input: n = 4, costs = [5,1,6,2]  |  Expected Output: 11
    inputs2 = {'n': 4, 'costs': [5, 1, 6, 2]}
    print(f'Test 2 Result:', solution.climbStairs(**inputs2), ' | Expected:', 11)

    # Example Input: n = 3, costs = [9,8,3]  |  Expected Output: 12
    inputs3 = {'n': 3, 'costs': [9, 8, 3]}
    print(f'Test 3 Result:', solution.climbStairs(**inputs3), ' | Expected:', 12)

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
