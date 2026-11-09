"""
This problem was extracted on 2026-11-09 08:00 (UTC+0) from LeetCode at https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/.
You can check the full problem description there.
Problem Title:
    Find Servers That Handled Most Number of Requests
Difficulty:
    Hard
Tags:
    Array, Heap (Priority Queue), Simulation, Ordered Set
"""

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Running the examples extracted from the problem statement:")
    print("-" * 40)
    # Example Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3]  |  Expected Output: [1]
    inputs1 = {'k': 3, 'arrival': [1, 2, 3, 4, 5], 'load': [5, 2, 3, 3, 3]}
    print(f'Test 1 Result:', solution.busiestServers(**inputs1), ' | Expected:', [1])

    # Example Input: k = 3, arrival = [1,2,3,4], load = [1,2,1,2]  |  Expected Output: [0]
    inputs2 = {'k': 3, 'arrival': [1, 2, 3, 4], 'load': [1, 2, 1, 2]}
    print(f'Test 2 Result:', solution.busiestServers(**inputs2), ' | Expected:', [0])

    # Example Input: k = 3, arrival = [1,2,3], load = [10,12,11]  |  Expected Output: [0,1,2]
    inputs3 = {'k': 3, 'arrival': [1, 2, 3], 'load': [10, 12, 11]}
    print(f'Test 3 Result:', solution.busiestServers(**inputs3), ' | Expected:', [0, 1, 2])

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
