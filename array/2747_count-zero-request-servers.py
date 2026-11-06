"""
This problem was extracted on 2026-11-06 07:56 (UTC+0) from LeetCode at https://leetcode.com/problems/count-zero-request-servers/.
You can check the full problem description there.
Problem Title:
    Count Zero Request Servers
Difficulty:
    Medium
Tags:
    Array, Hash Table, Sliding Window, Sorting
"""

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Running the examples extracted from the problem statement:")
    print("-" * 40)
    # Example Input: n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11]  |  Expected Output: [1,2]
    inputs1 = {'n': 3, 'logs': [[1, 3], [2, 6], [1, 5]], 'x': 5, 'queries': [10, 11]}
    print(f'Test 1 Result:', solution.countServers(**inputs1), ' | Expected:', [1, 2])

    # Example Input: n = 3, logs = [[2,4],[2,1],[1,2],[3,1]], x = 2, queries = [3,4]  |  Expected Output: [0,1]
    inputs2 = {'n': 3, 'logs': [[2, 4], [2, 1], [1, 2], [3, 1]], 'x': 2, 'queries': [3, 4]}
    print(f'Test 2 Result:', solution.countServers(**inputs2), ' | Expected:', [0, 1])

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
