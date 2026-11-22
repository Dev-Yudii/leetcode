"""
This problem was extracted on 2026-11-22 07:59 (UTC+0) from LeetCode at https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/.
You can check the full problem description there.
Problem Title:
    Check if All A's Appears Before All B's
Difficulty:
    Easy
Tags:
    String
"""

class Solution:
    def checkString(self, s: str) -> bool:
        pass

if __name__ == "__main__":
    solution = Solution()
    print("Running the examples extracted from the problem statement:")
    print("-" * 40)
    # Example Input: s = "aaabbb"  |  Expected Output: true
    inputs1 = {'s': 'aaabbb'}
    print(f'Test 1 Result:', solution.checkString(**inputs1), ' | Expected:', True)

    # Example Input: s = "abab"  |  Expected Output: false
    inputs2 = {'s': 'abab'}
    print(f'Test 2 Result:', solution.checkString(**inputs2), ' | Expected:', False)

    # Example Input: s = "bbb"  |  Expected Output: true
    inputs3 = {'s': 'bbb'}
    print(f'Test 3 Result:', solution.checkString(**inputs3), ' | Expected:', True)

"""
Notes:
    - Type your approach, insights and learnings here.
"""
# Add a line reading "# Solved" below when you finish the solution.
