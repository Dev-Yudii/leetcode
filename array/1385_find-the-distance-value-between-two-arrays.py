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
        ans = 0

        for i in arr1:
            for j in arr2:
                if abs(i - j) <= d:
                    break
            else:
                ans += 1

        return ans

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
    - Took me a long time to understand this problem... and I didn't by myself. One of the first comments 
"You're supposed to count the elements in arr1 that do NOT yield a value <= d when any element 
from arr2 is subtracted from it." from user Eti-ini Effiong-Robert
helped me to figure it out.
    - Once I understood the problem it was very simple, compare every element on array1 against array2, if
absolute value is higher than d, it isn't valid anymore, so we break the loop and go to the next
if all elements on array2 are valid, then we increment our ans variable by 1.

"""
# Add a line reading "# Solved" below when you finish the solution.
# Solved