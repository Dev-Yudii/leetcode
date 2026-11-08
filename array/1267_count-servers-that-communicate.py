"""
This problem was extracted on 2026-11-08 07:22 (UTC+0) from LeetCode at https://leetcode.com/problems/count-servers-that-communicate/.
You can check the full problem description there.
Problem Title:
    Count Servers that Communicate
Difficulty:
    Medium
Tags:
    Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix, Counting
"""

class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Running the examples extracted from the problem statement:")
    print("-" * 40)
    # Example Input: grid = [[1,0],[0,1]]  |  Expected Output: 0
    inputs1 = {'grid': [[1, 0], [0, 1]]}
    print(f'Test 1 Result:', solution.countServers(**inputs1), ' | Expected:', 0)

    # Example Input: grid = [[1,0],[1,1]]  |  Expected Output: 3
    inputs2 = {'grid': [[1, 0], [1, 1]]}
    print(f'Test 2 Result:', solution.countServers(**inputs2), ' | Expected:', 3)

    # Example Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]  |  Expected Output: 4
    inputs3 = {'grid': [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]}
    print(f'Test 3 Result:', solution.countServers(**inputs3), ' | Expected:', 4)

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
