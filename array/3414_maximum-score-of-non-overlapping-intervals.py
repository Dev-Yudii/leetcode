"""
This problem was extracted on 2026-11-05 11:16 (UTC+0) from LeetCode at https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/.
You can check the full problem description there.
Problem Title:
    Maximum Score of Non-overlapping Intervals
Difficulty:
    Hard
Tags:
    Array, Binary Search, Dynamic Programming, Sorting
"""

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]  |  Expected Output: [2,3]
    inputs1 = {'intervals': [[1, 3, 2], [4, 5, 2], [1, 5, 5], [6, 9, 3], [6, 7, 1], [8, 9, 1]]}
    print(f'Test 1 Result:', solution.maximumWeight(**inputs1), ' | Expected:', [2, 3])

    # Example Input: intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]  |  Expected Output: [1,3,5,6]
    inputs2 = {'intervals': [[5, 8, 1], [6, 7, 7], [4, 7, 3], [9, 10, 6], [7, 8, 2], [11, 14, 3], [3, 5, 5]]}
    print(f'Test 2 Result:', solution.maximumWeight(**inputs2), ' | Expected:', [1, 3, 5, 6])

"""
Notes:
    -
"""
