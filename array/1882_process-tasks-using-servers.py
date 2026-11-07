"""
This problem was extracted on 2026-11-07 07:12 (UTC+0) from LeetCode at https://leetcode.com/problems/process-tasks-using-servers/.
You can check the full problem description there.
Problem Title:
    Process Tasks Using Servers
Difficulty:
    Medium
Tags:
    Array, Heap (Priority Queue)
"""

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Running the examples extracted from the problem statement:")
    print("-" * 40)
    # Example Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]  |  Expected Output: [2,2,0,2,1,2]
    inputs1 = {'servers': [3, 3, 2], 'tasks': [1, 2, 3, 2, 1, 2]}
    print(f'Test 1 Result:', solution.assignTasks(**inputs1), ' | Expected:', [2, 2, 0, 2, 1, 2])

    # Example Input: servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]  |  Expected Output: [1,4,1,4,1,3,2]
    inputs2 = {'servers': [5, 1, 4, 3, 2], 'tasks': [2, 1, 2, 4, 5, 2, 1]}
    print(f'Test 2 Result:', solution.assignTasks(**inputs2), ' | Expected:', [1, 4, 1, 4, 1, 3, 2])

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
