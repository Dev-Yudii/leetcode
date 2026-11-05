"""
This problem was extracted on 2026-11-05 11:18 (UTC+0) from LeetCode at https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/.
You can check the full problem description there.
Problem Title:
    Find Two Non-overlapping Sub-arrays Each With Target Sum
Difficulty:
    Medium
Tags:
    Array, Hash Table, Binary Search, Dynamic Programming, Sliding Window
"""

class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: arr = [3,2,2,4,3], target = 3  |  Expected Output: 2
    inputs1 = {'arr': [3, 2, 2, 4, 3], 'target': 3}
    print(f'Test 1 Result:', solution.minSumOfLengths(**inputs1), ' | Expected:', 2)

    # Example Input: arr = [7,3,4,7], target = 7  |  Expected Output: 2
    inputs2 = {'arr': [7, 3, 4, 7], 'target': 7}
    print(f'Test 2 Result:', solution.minSumOfLengths(**inputs2), ' | Expected:', 2)

    # Example Input: arr = [4,3,2,6,2,3,4], target = 6  |  Expected Output: -1
    inputs3 = {'arr': [4, 3, 2, 6, 2, 3, 4], 'target': 6}
    print(f'Test 3 Result:', solution.minSumOfLengths(**inputs3), ' | Expected:', -1)

"""
Notes:
    -
"""
