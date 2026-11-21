"""
This problem was extracted on 2026-11-21 08:18 (UTC+0) from LeetCode at https://leetcode.com/problems/find-subtree-sizes-after-changes/.
You can check the full problem description there.
Problem Title:
    Find Subtree Sizes After Changes
Difficulty:
    Medium
Tags:
    Array, Hash Table, String, Tree, Depth-First Search
"""

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Running the examples extracted from the problem statement:")
    print("-" * 40)
    # Example Input: parent = [-1,0,0,1,1,1], s = "abaabc"  |  Expected Output: [6,3,1,1,1,1]
    inputs1 = {'parent': [-1, 0, 0, 1, 1, 1], 's': 'abaabc'}
    print(f'Test 1 Result:', solution.findSubtreeSizes(**inputs1), ' | Expected:', [6, 3, 1, 1, 1, 1])

    # Example Input: parent = [-1,0,4,0,1], s = "abbba"  |  Expected Output: [5,2,1,1,1]
    inputs2 = {'parent': [-1, 0, 4, 0, 1], 's': 'abbba'}
    print(f'Test 2 Result:', solution.findSubtreeSizes(**inputs2), ' | Expected:', [5, 2, 1, 1, 1])

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
