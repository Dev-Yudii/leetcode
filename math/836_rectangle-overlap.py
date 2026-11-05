"""
This problem was extracted on 2026-11-05 11:17 (UTC+0) from LeetCode at https://leetcode.com/problems/rectangle-overlap/.
You can check the full problem description there.
Problem Title:
    Rectangle Overlap
Difficulty:
    Easy
Tags:
    Math, Geometry
"""

class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]  |  Expected Output: true
    inputs1 = {'rec1': [0, 0, 2, 2], 'rec2': [1, 1, 3, 3]}
    print(f'Test 1 Result:', solution.isRectangleOverlap(**inputs1), ' | Expected:', True)

    # Example Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]  |  Expected Output: false
    inputs2 = {'rec1': [0, 0, 1, 1], 'rec2': [1, 0, 2, 1]}
    print(f'Test 2 Result:', solution.isRectangleOverlap(**inputs2), ' | Expected:', False)

    # Example Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]  |  Expected Output: false
    inputs3 = {'rec1': [0, 0, 1, 1], 'rec2': [2, 2, 3, 3]}
    print(f'Test 3 Result:', solution.isRectangleOverlap(**inputs3), ' | Expected:', False)

"""
Notes:
    -
"""
