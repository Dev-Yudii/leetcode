"""
This problem was extracted on 2026-10-25 08:58 (UTC-3) from LeetCode at https://leetcode.com/problems/number-of-closed-islands/.
You can check the full problem description there.
Problem Title:
    Number of Closed Islands
Difficulty:
    Medium
Tags:
    Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
"""

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]  |  Expected Output: 2
    inputs1 = {'grid': [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]}
    print(f'Test 1 Result:', solution.closedIsland(**inputs1), ' | Expected:', 2)

    # Example Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]  |  Expected Output: 1
    inputs2 = {'grid': [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]}
    print(f'Test 2 Result:', solution.closedIsland(**inputs2), ' | Expected:', 1)

    # Example Input: grid = [[1,1,1,1,1,1,1],  |  Expected Output: 2
    # (not auto-translated — write this test manually)

"""
Notes:
    -
"""
