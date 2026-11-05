"""
This problem was extracted on 2026-11-05 14:08 (UTC-3) from LeetCode at https://leetcode.com/problems/find-the-distance-value-between-two-arrays/.
You can check the full problem description there.
Problem Title:
    Find the Distance Value Between Two Arrays
Difficulty:
    Easy
Tags:
    Array, Two Pointers, Binary Search, Sorting
"""

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2  |  Expected Output: 2
    inputs1 = {'arr1': [4, 5, 8], 'arr2': [10, 9, 1, 8], 'd': 2}
    print(f'Test 1 Result:', solution.findTheDistanceValue(**inputs1), ' | Expected:', 2)

    # Example Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3  |  Expected Output: 2
    inputs2 = {'arr1': [1, 4, 2, 3], 'arr2': [-4, -3, 6, 10, 20, 30], 'd': 3}
    print(f'Test 2 Result:', solution.findTheDistanceValue(**inputs2), ' | Expected:', 2)

    # Example Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6  |  Expected Output: 1
    inputs3 = {'arr1': [2, 1, 100, 3], 'arr2': [-5, -2, 10, -3, 7], 'd': 6}
    print(f'Test 3 Result:', solution.findTheDistanceValue(**inputs3), ' | Expected:', 1)

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
