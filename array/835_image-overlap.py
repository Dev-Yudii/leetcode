"""
This problem was extracted on 2026-11-05 11:17 (UTC+0) from LeetCode at https://leetcode.com/problems/image-overlap/.
You can check the full problem description there.
Problem Title:
    Image Overlap
Difficulty:
    Medium
Tags:
    Array, Matrix
"""

class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]  |  Expected Output: 3
    inputs1 = {'img1': [[1, 1, 0], [0, 1, 0], [0, 1, 0]], 'img2': [[0, 0, 0], [0, 1, 1], [0, 0, 1]]}
    print(f'Test 1 Result:', solution.largestOverlap(**inputs1), ' | Expected:', 3)

    # Example Input: img1 = [[1]], img2 = [[1]]  |  Expected Output: 1
    inputs2 = {'img1': [[1]], 'img2': [[1]]}
    print(f'Test 2 Result:', solution.largestOverlap(**inputs2), ' | Expected:', 1)

    # Example Input: img1 = [[0]], img2 = [[0]]  |  Expected Output: 0
    inputs3 = {'img1': [[0]], 'img2': [[0]]}
    print(f'Test 3 Result:', solution.largestOverlap(**inputs3), ' | Expected:', 0)

"""
Notes:
    -
"""
