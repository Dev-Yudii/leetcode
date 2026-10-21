"""
This problem was extracted on 2026-10-21 12:05 (UTC-3) from LeetCode at https://leetcode.com/problems/minimum-operations-to-sort-a-string/.
You can check the full problem description there.
Problem Title:
    Minimum Operations to Sort a String
Difficulty:
    Medium
Tags:
    String
"""

class Solution:
    def minOperations(self, s: str) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Script generated! Configure your tests below:")
    print("-" * 40)
    # Example Input: s = "dog"  |  Expected Output: 1
    inputs1 = {}
    exec('s = "dog"', {}, inputs1)
    print(f'Test 1 Result:', solution.minOperations(**inputs1), ' | Expected:', '1')

    # Example Input: s = "card"  |  Expected Output: 2
    inputs2 = {}
    exec('s = "card"', {}, inputs2)
    print(f'Test 2 Result:', solution.minOperations(**inputs2), ' | Expected:', '2')

    # Example Input: s = "gf"  |  Expected Output: -1
    inputs3 = {}
    exec('s = "gf"', {}, inputs3)
    print(f'Test 3 Result:', solution.minOperations(**inputs3), ' | Expected:', '-1')

"""
Notes:
    -
"""
