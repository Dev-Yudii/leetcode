"""
This problem was extracted on 2026-11-05 11:16 (UTC+0) from LeetCode at https://leetcode.com/problems/unique-3-digit-even-numbers/.
You can check the full problem description there.
Problem Title:
    Unique 3-Digit Even Numbers
Difficulty:
    Easy
Tags:
    Array, Hash Table, Recursion, Enumeration
"""

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: digits = [1,2,3,4]  |  Expected Output: 12
    inputs1 = {'digits': [1, 2, 3, 4]}
    print(f'Test 1 Result:', solution.totalNumbers(**inputs1), ' | Expected:', 12)

    # Example Input: digits = [0,2,2]  |  Expected Output: 2
    inputs2 = {'digits': [0, 2, 2]}
    print(f'Test 2 Result:', solution.totalNumbers(**inputs2), ' | Expected:', 2)

    # Example Input: digits = [6,6,6]  |  Expected Output: 1
    inputs3 = {'digits': [6, 6, 6]}
    print(f'Test 3 Result:', solution.totalNumbers(**inputs3), ' | Expected:', 1)

    # Example Input: digits = [1,3,5]  |  Expected Output: 0
    inputs4 = {'digits': [1, 3, 5]}
    print(f'Test 4 Result:', solution.totalNumbers(**inputs4), ' | Expected:', 0)

"""
Notes:
    -
"""
