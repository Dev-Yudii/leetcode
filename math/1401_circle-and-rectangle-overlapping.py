"""
This problem was extracted on 2026-11-05 11:19 (UTC+0) from LeetCode at https://leetcode.com/problems/circle-and-rectangle-overlapping/.
You can check the full problem description there.
Problem Title:
    Circle and Rectangle Overlapping
Difficulty:
    Medium
Tags:
    Math, Geometry
"""

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1  |  Expected Output: true
    inputs1 = {'radius': 1, 'xCenter': 0, 'yCenter': 0, 'x1': 1, 'y1': -1, 'x2': 3, 'y2': 1}
    print(f'Test 1 Result:', solution.checkOverlap(**inputs1), ' | Expected:', True)

    # Example Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1  |  Expected Output: false
    inputs2 = {'radius': 1, 'xCenter': 1, 'yCenter': 1, 'x1': 1, 'y1': -3, 'x2': 2, 'y2': -1}
    print(f'Test 2 Result:', solution.checkOverlap(**inputs2), ' | Expected:', False)

    # Example Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1  |  Expected Output: true
    inputs3 = {'radius': 1, 'xCenter': 0, 'yCenter': 0, 'x1': -1, 'y1': 0, 'x2': 0, 'y2': 1}
    print(f'Test 3 Result:', solution.checkOverlap(**inputs3), ' | Expected:', True)

"""
Notes:
    -
"""
