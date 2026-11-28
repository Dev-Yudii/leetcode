"""
This problem was extracted on 2026-11-28 08:55 (UTC+0) from LeetCode at https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/.
You can check the full problem description there.
Problem Title:
    Maximum Number of Items From Sale II
Difficulty:
    Medium
Tags:
    Array, Greedy, Sorting, Heap (Priority Queue)
"""

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Running the examples extracted from the problem statement:")
    print("-" * 40)
    # Example Input: items = [[1,6],[2,4],[3,5]], budget = 19  |  Expected Output: 5
    inputs1 = {'items': [[1, 6], [2, 4], [3, 5]], 'budget': 19}
    print(f'Test 1 Result:', solution.maximumSaleItems(**inputs1), ' | Expected:', 5)

    # Example Input: items = [[2,8],[1,10],[6,6],[4,12],[5,20],[5,17]], budget = 35  |  Expected Output: 7
    inputs2 = {'items': [[2, 8], [1, 10], [6, 6], [4, 12], [5, 20], [5, 17]], 'budget': 35}
    print(f'Test 2 Result:', solution.maximumSaleItems(**inputs2), ' | Expected:', 7)

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
