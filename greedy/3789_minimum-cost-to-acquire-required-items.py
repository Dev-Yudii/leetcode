"""
This problem was extracted on 2026-11-11 07:45 (UTC+0) from LeetCode at https://leetcode.com/problems/minimum-cost-to-acquire-required-items/.
You can check the full problem description there.
Problem Title:
    Minimum Cost to Acquire Required Items
Difficulty:
    Medium
Tags:
    Math, Greedy
"""

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Running the examples extracted from the problem statement:")
    print("-" * 40)
    # Example Input: cost1 = 3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2  |  Expected Output: 3
    inputs1 = {'cost1': 3, 'cost2': 2, 'costBoth': 1, 'need1': 3, 'need2': 2}
    print(f'Test 1 Result:', solution.minimumCost(**inputs1), ' | Expected:', 3)

    # Example Input: cost1 = 5, cost2 = 4, costBoth = 15, need1 = 2, need2 = 3  |  Expected Output: 22
    inputs2 = {'cost1': 5, 'cost2': 4, 'costBoth': 15, 'need1': 2, 'need2': 3}
    print(f'Test 2 Result:', solution.minimumCost(**inputs2), ' | Expected:', 22)

    # Example Input: cost1 = 5, cost2 = 4, costBoth = 15, need1 = 0, need2 = 0  |  Expected Output: 0
    inputs3 = {'cost1': 5, 'cost2': 4, 'costBoth': 15, 'need1': 0, 'need2': 0}
    print(f'Test 3 Result:', solution.minimumCost(**inputs3), ' | Expected:', 0)

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
